# Tests for the i-Nav graph, pathfinding and API.
# Run from inav-2/backend:  python -m unittest -v test_app
# Importing app parses all five DXF floor plans, so loading takes a little while.

import itertools
import os
import random
import re
import tempfile
import unittest

import ezdxf
import networkx as nx

import app

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_JS = os.path.join(BASE_DIR, "..", "frontend", "script.js")

INTER_FLOOR = {frozenset((u, v)) for u, v, _ in app.inter_floor_edges}

# Rooms that exist in the DXF plans but have no edge in any floor's edge list.
# No source data justifies connecting them, so they are expected to be unreachable.
KNOWN_ISOLATED_ROOMS = {"11AC1009", "11AC2038", "11AC2023", "11AC3028", "11AC4002", "11AC4034"}
# Same for these "DN" stair labels, which the frontend lists but no edge list uses.
KNOWN_UNCONNECTED_STAIRS = {"f0stair3", "f0stair4", "f0stair5", "f0stair6", "f1stair3", "f1stair4",
                            "f2stair5", "f2stair6", "f2stair7", "f2stair8", "f2stair9", "f2stair10"}


def floor_of(node):
    match = re.match(r"^(?:11AC([G0-9])|f([0-9]))", node)
    if not match:
        return None
    digit = match.group(1) or match.group(2)
    return 0 if digit == "G" else int(digit)


def frontend_room_list():
    with open(SCRIPT_JS, encoding="utf-8") as f:
        js = f.read()
    active = js[js.index("\n document.addEventListener"):]
    list_src = active[active.index("[") + 1:active.index("];")]
    list_src = re.sub(r"//.*", "", list_src)
    return re.findall(r'"([^"]+)"', list_src)


def path_cost(path):
    return sum(app.G[u][v]["weight"] for u, v in zip(path, path[1:]))


def assert_valid_route(test, path, start, end):
    test.assertIsNotNone(path, f"no path {start} -> {end}")
    test.assertEqual(path[0], start)
    test.assertEqual(path[-1], end)
    for u, v in zip(path, path[1:]):
        test.assertTrue(app.G.has_edge(u, v), f"{u} -> {v} is not a graph edge")
        if floor_of(u) != floor_of(v):
            test.assertIn(frozenset((u, v)), INTER_FLOOR, f"floor jump {u} -> {v} is not a lift/stair edge")


class TestGraphStructure(unittest.TestCase):

    def test_every_node_is_floor_namespaced(self):
        bad = [n for n in app.G.nodes if floor_of(n) is None]
        self.assertEqual(bad, [])

    def test_no_nodes_merged_across_floors(self):
        floor_nodes = [app.floor0_nodes, app.floor1_nodes, app.floor2_nodes, app.floor3_nodes, app.floor4_nodes]
        self.assertEqual(app.G.number_of_nodes(), sum(len(n) for n in floor_nodes))

    def test_inter_floor_edges_reference_real_nodes(self):
        for u, v, _ in app.inter_floor_edges:
            for node in (u, v):
                self.assertIn("pos", app.G.nodes[node], f"{node} was not extracted from a DXF plan")

    def test_floors_connect_only_through_lifts_and_stairs(self):
        for u, v in app.G.edges:
            if floor_of(u) != floor_of(v):
                self.assertIn(frozenset((u, v)), INTER_FLOOR)
                self.assertTrue(re.search("lift|stair", u) and re.search("lift|stair", v), (u, v))

    def test_known_isolated_rooms(self):
        isolated = {n for n in app.G.nodes if app.G.degree(n) == 0 and n.startswith("11AC")}
        self.assertEqual(isolated, KNOWN_ISOLATED_ROOMS)

    def test_cafe_is_renamed_to_room_id(self):
        self.assertIn("11AC4028", app.G)


class TestRouting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        main = max(nx.connected_components(app.G), key=len)
        cls.rooms = sorted(n for n in main if n.startswith("11AC"))
        cls.nodes = sorted(main)

    def route(self, start, end):
        path, cost = app.dijkstra(app.adj_list, start, end)
        assert_valid_route(self, path, start, end)
        self.assertAlmostEqual(cost, path_cost(path))
        return path, cost

    def test_ground_to_first_floor(self):
        self.route("11ACG004", "11AC1010")

    def test_ground_to_fourth_floor(self):
        path, cost = self.route("11ACG004", "11AC4013")
        # Before the fix this went through a lift_lobby1 node shared by all floors (cost 32.03)
        self.assertTrue(any("lift" in n or "stair" in n for n in path))
        self.assertGreater(cost, 32.03)

    def test_every_floor_pair(self):
        by_floor = {}
        for room in self.rooms:
            by_floor.setdefault(floor_of(room), room)
        self.assertEqual(sorted(by_floor), [0, 1, 2, 3, 4])
        for a, b in itertools.permutations(by_floor, 2):
            with self.subTest(floors=(a, b)):
                self.route(by_floor[a], by_floor[b])

    def test_lift_and_stair_endpoints(self):
        self.route("f0lift1", "f4lift1")
        self.route("f0stair1", "11AC3021")

    def test_random_routes_use_real_edges_and_costs(self):
        rng = random.Random(1)
        for _ in range(2000):
            start, end = rng.sample(self.nodes, 2)
            self.route(start, end)

    def test_same_start_and_end(self):
        self.assertEqual(app.dijkstra(app.adj_list, "11AC2004", "11AC2004"), (["11AC2004"], 0))

    def test_unreachable_room(self):
        self.assertEqual(app.dijkstra(app.adj_list, "11AC1009", "11ACG004"), (None, float("inf")))

    def test_matches_networkx(self):
        rng = random.Random(2)
        all_nodes = sorted(app.G.nodes)
        for _ in range(5000):
            start, end = rng.sample(all_nodes, 2)
            _, cost = app.dijkstra(app.adj_list, start, end)
            try:
                expected = nx.dijkstra_path_length(app.G, start, end)
            except nx.NetworkXNoPath:
                expected = float("inf")
            self.assertAlmostEqual(cost, expected, msg=f"{start} -> {end}")


class TestApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.app.test_client()

    def get(self, start, end):
        return self.client.get("/shortest-path", query_string={"start": start, "end": end})

    def test_valid_route(self):
        res = self.get("11ACG004", "11AC4013")
        self.assertEqual(res.status_code, 200)
        body = res.get_json()
        assert_valid_route(self, body["path"], "11ACG004", "11AC4013")
        self.assertAlmostEqual(body["time"], path_cost(body["path"]))

    def test_case_insensitive_input(self):
        for start, end in [("F0LIFT1", "f4lift1"), ("11acg004", "11ac1010"), ("  F2Stair1 ", "11AC3021")]:
            with self.subTest(start=start, end=end):
                res = self.get(start, end)
                self.assertEqual(res.status_code, 200)
                path = res.get_json()["path"]
                self.assertEqual(path[0], app.node_lookup[start.strip().upper()])

    def test_missing_params(self):
        self.assertEqual(self.get("", "11AC4013").status_code, 400)
        self.assertEqual(self.client.get("/shortest-path").status_code, 400)

    def test_invalid_location(self):
        res = self.get("NOT_A_ROOM", "11AC4013")
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.get_json()["error"], "Invalid node")

    def test_generic_names_are_not_routable(self):
        # Unprefixed names like lift_lobby1 used to be one node shared by every floor
        self.assertEqual(self.get("lift_lobby1", "11AC4013").status_code, 400)

    def test_unreachable_room(self):
        res = self.get("11AC1009", "11ACG004")
        self.assertEqual(res.status_code, 404)


class TestFrontendRoomList(unittest.TestCase):

    def test_every_listed_location_is_in_graph(self):
        rooms = frontend_room_list()
        self.assertGreater(len(rooms), 200)
        missing = [r for r in rooms if r not in app.G]
        self.assertEqual(missing, [])

    def test_case_insensitive_lookup_is_unambiguous(self):
        self.assertEqual(len(app.node_lookup), app.G.number_of_nodes())
        rooms = frontend_room_list()
        self.assertEqual(len({r.lower() for r in rooms}), len(set(rooms)))

    def test_lifts_and_stairs_are_listed_and_reachable(self):
        main = max(nx.connected_components(app.G), key=len)
        vertical = [r for r in frontend_room_list() if "lift" in r or "stair" in r]
        self.assertGreater(len(vertical), 50)
        unreachable = {r for r in vertical if r not in main}
        self.assertEqual(unreachable, KNOWN_UNCONNECTED_STAIRS)

    def test_listed_locations_outside_graph_are_only_known_gaps(self):
        main = max(nx.connected_components(app.G), key=len)
        unreachable = {r for r in frontend_room_list() if r not in main}
        self.assertEqual(unreachable, KNOWN_ISOLATED_ROOMS | KNOWN_UNCONNECTED_STAIRS)


class TestDxfExtraction(unittest.TestCase):

    def extract(self, labels):
        doc = ezdxf.new()
        msp = doc.modelspace()
        for i, label in enumerate(labels):
            msp.add_text(label, dxfattribs={"insert": (i * 10, 0)})
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "plan.dxf")
            doc.saveas(path)
            return app.extract_nodes(path)

    def test_staircase_labels(self):
        nodes = self.extract(["ST1", "st12", "ST 3", "STORE"])
        self.assertEqual(nodes, {"staircase1": (0, 0), "staircase2": (10, 0), "store1": (30, 0)})

    def test_room_categories(self):
        nodes = self.extract(["LIFT LOBBY", "LIFT", "LAB", "DN", "PLANTER", "R.SCHOLAR", "COURT YARD", "CAFE"])
        self.assertEqual(sorted(nodes), ["cafe1", "lab1", "lift1", "lift_lobby1", "scholar1", "stair1", "stair_up1"])


if __name__ == "__main__":
    unittest.main()
