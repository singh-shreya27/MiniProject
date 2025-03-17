import ezdxf
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

# Function to extract nodes from DXF file
def extract_nodes(msp):
    nodes = {}
    category_count = defaultdict(int)

    # Keywords for room types
    keywords = {
        "class": "CLASS",
        "lab": "LAB",
        "ahu": "AHU",
        "staircase": "ST",
        "lift_lobby": "LIFT LOBBY",
        "room": "ROOM",
        "toilet": "TOILET",
        "entrance_lobby": "ENTRANCE LOBBY",
        "lift": "LIFT",
        "r_scholar_lab": "R.SCHOLAR LAB",
        "spare_room": "SPARE ROOM"
    }

    for entity in msp:
        if entity.dxftype() in ["TEXT", "MTEXT"]:
            text = entity.dxf.text.strip().upper()
            position = (entity.dxf.insert.x, entity.dxf.insert.y)

            if "COURT YARD" in text:
                continue  # Skip courtyard nodes

            for key, identifier in keywords.items():
                if identifier in text:
                    category_count[key] += 1
                    node_name = f"{key}{category_count[key]}"
                    nodes[node_name] = position
                    break

    # Manually adjust positions for specific overlapping nodes
    offset_x, offset_y = 10, 10  # Increased offset to prevent overlap
    if "lift_lobby3" in nodes:
        nodes["Staircase_Left_LiftLobby3"] = (nodes["lift_lobby3"][0] - offset_x, nodes["lift_lobby3"][1] + offset_y)
    if "lift_lobby4" in nodes:
        nodes["Staircase_Right_LiftLobby4"] = (nodes["lift_lobby4"][0] + offset_x, nodes["lift_lobby4"][1] + offset_y)
    if "ahu8" in nodes:
        nodes["SpareRoom_Right_AHU8"] = (nodes["ahu8"][0] + offset_x, nodes["ahu8"][1] - offset_y)
        nodes["Staircase_Left_AHU8"] = (nodes["ahu8"][0] - offset_x, nodes["ahu8"][1] + offset_y)
    if "ahu9" in nodes:
        nodes["SpareRoom_Left_AHU9"] = (nodes["ahu9"][0] - offset_x, nodes["ahu9"][1] - offset_y)
        nodes["Staircase_Right_AHU9"] = (nodes["ahu9"][0] + offset_x, nodes["ahu9"][1] + offset_y)
    if "room10" in nodes:
        nodes["RScholLab_Right_Room10_1"] = (nodes["room10"][0] + offset_x, nodes["room10"][1] + offset_y)
        nodes["RScholLab_Right_Room10_2"] = (nodes["room10"][0] + offset_x, nodes["room10"][1] - offset_y)
        nodes["RScholLab_Left_Room10_1"] = (nodes["room10"][0] - offset_x, nodes["room10"][1] + offset_y)
        nodes["RScholLab_Left_Room10_2"] = (nodes["room10"][0] - offset_x, nodes["room10"][1] - offset_y)

    return nodes

# Function to create edges between specific nodes
def create_edges():
    edges = [
        ("ahu8", "lab2",3),
        ("lab2", "lab1",4),
        ("ahu8", "ahu9",15),
        ("ahu9", "lab4",3),
        ("lab4", "lab3",4),
        ("toilet3", "toilet4",1),
        ("toilet1", "toilet2", 1),
        ("toilet2", "room1", 2),
        ("room1", "room2", 4),
        ("room2", "room6", 1),
        ("lift1", "lift2", 1),
        ("lab7", "lab8", 2),
        ("lab5", "lab6", 2),
        ("ahu4", "lab5", 1),
        ("ahu4", "lab7", 1),
        ("lab6", "ahu3", 1),
        ("ahu3", "lab8", 1),
        ("toilet4","room3",2),
        ("room3","room5",3),
        ("room3","room4",4),
        ("room5","room6",6),
        ("lift3","lift4",1),
        ("lift_lobby4","lift3",1),
        ("lift_lobby2","lift8",1),
        ("lift8","lift7",1),
        ("lift6","lift5",1),
        ("lift_lobby1","lift6",1),
        ("lift_lobby1","lift5",1),
        ("lift_lobby1","lift5",1),
        ("lift_lobby2","lift8",1),
        ("lift_lobby2","lift7",1),
        ("toilet5","toilet6",1),
        ("toilet7","toilet8",1),
        ("staircase1","room10",10),
        ("staircase3","room10",10),
        ("staircase2","staircase1",8),
        ("staircase3","staircase2",8),
        ("ahu7","staircase3",2),
        ("staircase1","ahu2",2),
        ("staircase1","staircase3",15),
        ("ahu7","toilet7",2),
        ("ahu7","toilet8",2.5),
        ("ahu2","toilet5",2),
        ("ahu2","toilet6",2.5),
        ("room8","toilet6",4),
        ("room8","lift6",2),
        ("lift_lobby1","lab6",3),
        ("lift_lobby2","lab10",3),
        ("lab10", "lab9", 2),
        ("lab11", "lab12", 2),
        ("ahu5", "lab10", 1),
        ("ahu5", "lab12", 1),
        ("lab11", "ahu6", 1),
        ("ahu6", "lab9", 1),
        ("toilet8","room7",4),
        ("room7","lift7",2),
        ("lab8","room6",3),
        ("lab8","room1",3),
        ("lab12","room5",3),
        ("lab12","room3",3),
        ("lift_lobby4","room5",3),
        ("lift_lobby4","room3",3),
        ("lift_lobby3","room6",3),
        ("lift_lobby3","room1",3),
        ("lab2","room1",4),
        ("lab4","room3",4),

        
        
    ]
    return edges

# Function to visualize nodes and edges
def visualize_graph(nodes, edges):
    plt.figure(figsize=(12, 8))
    for name, pos in nodes.items():
        plt.scatter(*pos, s=100, color='blue')
        plt.text(pos[0], pos[1], name, fontsize=8, ha='right', va='bottom')
    
    for edge in edges:
        if len(edge) == 2:
            node1, node2 = edge
            weight = None
        else:
            node1, node2, weight = edge
        
        if node1 in nodes and node2 in nodes:
            x_values = [nodes[node1][0], nodes[node2][0]]
            y_values = [nodes[node1][1], nodes[node2][1]]
            plt.plot(x_values, y_values, 'k-', linewidth=1)
            if weight:
                plt.text((x_values[0] + x_values[1]) / 2, (y_values[0] + y_values[1]) / 2, str(weight), fontsize=8, color='red')
    
    plt.title("Graph Visualization with Nodes and Connections")
    plt.xlabel("X Coordinates")
    plt.ylabel("Y Coordinates")
    plt.grid(True)
    plt.show()

# Main function
def main(dxf_file_path):
    doc = ezdxf.readfile(dxf_file_path)
    msp = doc.modelspace()

    nodes = extract_nodes(msp)
    edges = create_edges()
    
    print(f"Extracted Nodes: {len(nodes)}")
    for name, pos in nodes.items():
        print(f"{name}: {pos}")
    
    visualize_graph(nodes, edges)

# Example usage (Replace with your DXF file path)
dxf_file_path = r"C:\Users\shrey\OneDrive\Desktop\floor2.dxf"
main(dxf_file_path)
