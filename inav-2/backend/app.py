## FINAL PROJECT PROGRAM

import ezdxf
import networkx as nx
import matplotlib.pyplot as plt
import re
from collections import defaultdict
import sys

# Step 1: Extract Nodes from DXF

def extract_nodes(dxf_file_path):
    doc = ezdxf.readfile(dxf_file_path)
    msp = doc.modelspace()
    nodes = {}
    category_count = defaultdict(int)

    keywords = {
        "class": "CLASS",
        "lab": "LAB",
        "ahu": "AHU",
        "lift_lobby": "LIFT LOBBY",
        "room": "ROOM",
        "toilet": "TOILET",
        "entrance_lobby": "ENTRANCE LOBBY",
        "lift": "LIFT",
        "spare_room": "SPARE ROOM",
        "mlab": "75 MM SUNKEN M.LAB",
        "40c": "40S. CLASS",
        "scholar": "SCHOLAR",
        "60c": "60S. CLASS",
        "faculty": "FACULTY",
        "meet": "MEETING",
        "store": "STORE",
        "cafe": "CAFE"
    }

    for entity in msp:
        if entity.dxftype() in ["TEXT", "MTEXT"]:
            text = entity.dxf.text.strip().upper()
            position = (entity.dxf.insert.x, entity.dxf.insert.y)

            if "COURT YARD" in text:
                continue

            match = re.match(r"ST(\\d+)", text)
            if match:
                category_count["staircase"] += 1
                node_name = f"staircase{category_count['staircase']}"
                nodes[node_name] = position
                continue

            if "DN" in text:
                category_count["stair_dn"] += 1
                node_name = f"stair{category_count['stair_dn']}"
                nodes[node_name] = position
                continue

            if "PLANTER" in text:
                category_count["st_up"] += 1
                node_name = f"stair_up{category_count['st_up']}"
                nodes[node_name] = position
                continue

            if "R.SCHOLAR" in text:
                category_count["scholar"] += 1
                node_name = f"scholar{category_count['scholar']}"
                nodes[node_name] = position
                continue

            for key, identifier in keywords.items():
                if identifier in text:
                    category_count[key] += 1
                    node_name = f"{key}{category_count[key]}"
                    nodes[node_name] = position
                    break

    return nodes

# Step 2: Create Graph and Add Nodes and Edges

def add_nodes_edges(G, nodes, edges):
    G.add_nodes_from([(node, {"pos": pos}) for node, pos in nodes.items()])
    G.add_weighted_edges_from(edges)

# Step 3: Rename Nodes After Adding Connections

def rename_graph_nodes(G, rename_map):
    mapping = {node: rename_map.get(node, node) for node in G.nodes()}
    nx.relabel_nodes(G, mapping, copy=False)

G = nx.Graph()

# Floor 0
import os

base_path = "floors"
dxf_f0 = os.path.join(base_path, "floor0.dxf")
dxf_f1 = os.path.join(base_path, "floor1.dxf")
dxf_f2 = os.path.join(base_path, "floor2.dxf")
dxf_f3 = os.path.join(base_path, "floor3.dxf")
dxf_f4 = os.path.join(base_path, "floor4.dxf")



floor0_nodes = extract_nodes(dxf_f0)
floor0_edges = [
 ("lift_lobby1", "lift1", 2),

        ("lift_lobby1", "lift2", 2),

        ("lift_lobby2", "lift3", 2),

        ("lift_lobby2", "lift4", 2),

        ("lift4", "lift3", 2),

        ("lift1", "lift2", 2),

        ("toilet1", "toilet2", 1),

        ("toilet3", "toilet4", 1),

        ("entrance_lobby1", "ahu1", 15),

        ("lab1", "ahu1", 12.2),

        ("lab2", "ahu2", 2.2),

        ("entrance_lobby1", "room1", 12),
        ("entrance_lobby1", "stair_up2", 3),

        ("room1", "ahu2", 4.43),

        ("room3", "toilet2", 20),

        ("lift_lobby1", "room3", 11),

       ("lift_lobby1", "room2", 9.37),

        ("room2", "room3", 1.37),

        ("room4", "toilet4", 9.44),
   
        ("lift_lobby2", "room5", 7),

        ("room5", "room4", 1.74),

        ("room2", "ahu1", 6.46),

        ("room5", "ahu2", 8.5),

        ("ahu1", "toilet2", 10),

        ("ahu2", "toilet4", 10.24),

        ("stair1","room2",9),

        ("stair1","room3",8.5),

        ("stair2","room5",8.5),

        ("stair2","room4",9),

        ("stair_up2","stair_up3",1),

   
   
]
add_nodes_edges(G, floor0_nodes, floor0_edges)

rename_map_floor0 = {
    "ahu1": "11ACG002",
    "lab1": "11ACG004",
    "lab2": "11ACG010",
    "room1": "11ACG008",
    "ahu2": "11ACG009",
    "room2": "11ACG006",
    "room3": "11ACG005",
    "room5": "11ACG013",
    "room4": "11ACG012",
    "lift1": "f0lift1",
    "lift2": "f0lift2",
    "lift3": "f0lift3",
    "lift4": "f0lift4",
    "stair1": "f0stair1",
    "stair2": "f0stair2",
    "stair3": "f0stair3",
    "stair4": "f0stair4",
    "stair5": "f0stair5",
    "stair6": "f0stair6",
    "stair7": "f0stair7",
    "stair_up1":"f0stair_up1",
    "stair_up2":"f0stair_up2",
    "stair_up3":"f0stair_up3",
    "stair_up4":"f0stair_up4",
    "stair_up5":"f0stair_up5",
    "stair_up6":"f0stair_up6",

}
rename_graph_nodes(G, rename_map_floor0)

# Floor 1
floor1_nodes = extract_nodes(dxf_f1)
# Floor 1
floor1_nodes = extract_nodes(dxf_f1)
floor1_edges = [
("lab6", "lab5", 9.77),

        ("room4", "room5", 2.05),

        ("room5", "lab2", 4.91),

        ("room4", "room6", 3.14),

        ("lab1","lab2",9.02),

        ("lab4","lab3",8.20),

        ("toilet2","toilet3",1),

        ("lift2","lift1",1),

        ("lift_lobby1","lift1",2),

        ("lift_lobby1","lift2",2),            

        ("lift_lobby2","lift3",2),            

        ("lift_lobby2","lift4",2),

        ("lift4","lift3",2),

        ("lab10","lab9",9.62),

        ("lab10","ahu5",11.13),

        ("lab12","ahu5",10.64),

        ("lab9","ahu6",36),

        ("lab6","ahu3",11.83),

        ("lab8","ahu3",12.04),

        ("lab8","lab7",8.86),
                               
        ("room6","toilet3",9.16),                          

        ("room2","toilet1",9.16),                          

        ("lab12","lab11",9.30),                          

        ("ahu2","lab4",2.26),                          

        ("ahu2","ahu1",29.91),                          

        ("ahu1","lab2",2.92),                          

        ("toilet3","lab2",8.71),                          

        ("toilet1","lab4",9.07),                          

         ("room2","room3",3.73),                          

        ("room7","room3",1.90),                          

        ("room7","lab4",4.84),                          

        ("lift_lobby2","room3",10.68),                          

        ("lift_lobby1","room4",11),                          

        ("lift_lobby2","lab12",3.73),                          

        ("lift_lobby1","lab8",3.62),                          

        ("lift_lobby1","lift_lobby2",60),   

        ("stair1","lab8",7),    
        ("stair1","room4",6.4),    

        ("stair1","lab7",12),    

        ("stair2","lab12",6.3),    

        ("stair2","room3",6.4),

        ("stair_up1","stair_up2",1),    
]
add_nodes_edges(G, floor1_nodes, floor1_edges)

rename_map_floor1 = {
      "ahu1": "11AC1002",
        "ahu2": "11AC1015",
        "lab4": "11AC1016",
        "lab3": "11AC1017",
         "room5":"11AC1007",
         "room6":"11AC1005",
         "room4":"11AC1006",
         "room3":"11AC1019",
         "room7":"11AC1020",
         "room2":"11AC1018",
         "lab8":"11AC1010",
         "lab6":"11AC1012",
         "lab7":"11AC1008",
         "lab9":"11AC1026",
         "lab10":"11AC1025",
         "lab12":"11AC1023",
         "ahu3":"11AC1011",
         "ahu5":"11AC1024",
         "ahu6":"11AC1022",
         "ahu4":"11AC1009",
         "lab11":"11AC1021",
         "lab1":"11AC1004",
         "lab2":"11AC1003",
         "lab5":"11AC1013",
          "lift1":"f1lift1",
        "lift2":"f1lift2",
        "lift3":"f1lift3",
        "lift4":"f1lift4",
        "stair1":"f1stair1",
        "stair2":"f1stair2",
        "stair3":"f1stair3",
        "stair4":"f1stair4",
         "stair_up1":"f1stair_up1",
    "stair_up2":"f1stair_up2",
        }
rename_graph_nodes(G, rename_map_floor1)

# Floor 2
floor2_nodes = extract_nodes(dxf_f2)
floor2_edges = [
   ("scholar1", "scholar2", 7.73),

    ("scholar3", "scholar4", 8.36),

    ("room10", "scholar2", 4.71),

    ("room10", "scholar4", 17.6),

    ("ahu8", "lab2", 3.24),

    ("lab2", "lab1", 8.56),

    ("ahu8", "ahu9", 15),

    ("ahu9", "lab4", 3.45),

    ("lab4", "lab3", 8.35),

    ("toilet3", "toilet4", 1),

    ("toilet1", "toilet2", 1),

    ("toilet2", "room1", 9.33),

    ("room1", "room2", 3),

    ("room2", "room6", 2.67),

    ("lift1", "lift2", 2),

    ("lab7", "lab8", 7.8),

    ("lab5", "lab6", 9),

    ("ahu4", "lab5", 5.8),

    ("ahu4", "lab7", 6.28),

    ("lab6", "ahu3", 10.77),

    ("ahu3", "lab8", 1),

    ("toilet4", "room3", 9.63),

    ("room3", "room5", 2.54),

    ("room3", "room4", 2.32),

    ("room5", "room6", 6),

    ("lift3", "lift4", 2),

    ("lift_lobby4", "lift3", 2),

    ("lift_lobby2", "lift8", 2),

    ("lift8", "lift7", 2),

    ("lift6", "lift5", 2),

    ("lift_lobby1", "lift6", 2),

    ("lift_lobby1", "lift5", 2),

    ("toilet5", "toilet6", 1),

    ("toilet7", "toilet8", 1),

    ("ahu7", "toilet7", 19),

    ("ahu7", "toilet8", 19.7),

    ("ahu2", "toilet5", 17.6),

    ("toilet5", "toilet6", 1),

    ("room8", "toilet6", 5.5),

    ("room8", "lift6", 11.5),

    ("lift_lobby1", "lab6", 3.5),

    ("lift_lobby2", "lab10", 3),

    ("lab10", "lab9", 2),

    ("lab11", "lab12", 9.23),

    ("ahu5", "lab10", 11.41),

    ("ahu5", "lab12", 10.76),

    ("toilet8", "room7", 7.3),

    ("room7", "lift7", 12.23),

    ("lab8", "room6", 9.61),

    ("lab8", "room1", 9.89),

    ("lab12", "room5", 8.25),

    ("lab12", "room3", 9.14),

    ("lift_lobby4", "room5", 3),

    ("lift_lobby4", "room3", 12.33),

    ("lift_lobby3", "room6", 3),

    ("lift_lobby3", "room1", 12.63),

    ("lab4", "room3", 6.58),

    ("scholar1", "ahu2", 5.42),

    ("scholar3", "ahu7", 6.25),

   

    ("room9", "ahu1", 5.42),

    ("room9", "room10", 13.55),

    ("room9", "room7", 3),

    ("room9", "scholar4", 10),

    ("ahu1", "room10", 8.61),

    ("stair_up1","stair_up2",1),

    ("stair_up3","stair_up2",1),
    ("stair_up4","room10",3),

    ("stair4","room8",7.32),

    ("stair4","lab6",5.37),

    ("stair1","room7",10.2),

    ("stair1","lab10",7.6),

    ("stair2","lab8",7.5),

    ("stair2","room1",11),

    ("stair3","lab12",8),

    ("stair3","room3",9.7),

    ("stair_up4","stair_up6",1),

    ("stair_up4","stair_up5",1),

    ("stair_up4","stair_up3",1),
]



add_nodes_edges(G, floor2_nodes, floor2_edges)

rename_map_floor2 = {
     "lab2": "11AC2004", "lab1": "11AC2005", "ahu8": "11AC2003", "ahu7": "11AC2028",
        "ahu9": "11AC2044", "ahu5": "11AC2035", "ahu6": "11AC2038", "ahu4": "11AC2010",
        "ahu3": "11AC2012", "ahu2": "11AC2019", "scholar1": "11AC2020", "scholar2": "11AC2021",
        "scholar4": "11AC2026", "scholar3": "11AC2027", "lab4": "11AC2043", "lab6": "11AC2013",
        "lab5": "11AC2014", "lab7": "11AC2009", "lab8": "11AC2011", "lab3": "11AC2042",
        "room6": "11AC2007", "room5": "11AC2040", "room4": "11AC2039", "room3": "11AC2041",
        "room7": "11AC2031", "room2": "11AC2008", "room1": "11AC2006", "room8": "11AC2016",
        "lab10": "11AC2034", "lab9": "11AC2033", "lab12": "11AC2036", "lab11": "11AC2037","room10":"11AC2022",
        "store1":"11AC2023","ahu1":"11AC2024","room9":"11AC2025","lift1":"f2lift1","lift2":"f2lift2",
        "lift3":"f2lift3","lift4":"f2lift4","lift5":"f2lift5","lift6":"f2lift6","lift7":"f2lift7","lift8":"f2lift8","stair1":"f2stair1","stair2":"f2stair2","stair3":"f2stair3","stair4":"f2stair4","stair5":"f2stair5","stair6":"f2stair6","stair7":"f2stair7","stair8":"f2stair8","stair9":"f2stair9","stair10":"f2stair10",
         "stair_up1":"f2stair_up1",
    "stair_up2":"f2stair_up2",
    "stair_up3":"f2stair_up3",
    "stair_up4":"f2stair_up4",
    "stair_up5":"f2stair_up5",
    "stair_up6":"f2stair_up6",
  
}
rename_graph_nodes(G, rename_map_floor2)

# Floor 3
floor3_nodes = extract_nodes(dxf_f3)
floor3_edges = []
    # Floor 3
floor3_nodes = extract_nodes(dxf_f3)
floor3_edges = [
      ("class1", "class2", 8.44),

         ("ahu1", "ahu2", 3.8),

        ("ahu1", "lab1", 14),

        ("ahu2", "lab1", 9.37),

        ("lab1", "lab2", 14.61),

        ("ahu3", "class4", 2.27),

        ("class4", "class3", 7.69),

        ("lift4", "lift3", 2),

        ("lift_lobby4", "lift4", 2),

        ("lift_lobby4", "lift3", 2),

        ("class4", "toilet8", 8.56),

        ("toilet8", "toilet7", 1),

        ("room6", "room7", 2.96),

        ("room6", "lift_lobby4", 10.11),

        ("room5", "lift_lobby4", 12.06),

        ("room5", "class4", 7.7),

        ("lab8", "lab7", 10.21),

        ("lab8", "ahu7", 8.07),

        ("lab10", "ahu7", 9.30),

        ("lab10", "lab9", 8.59),

        ("faculty6", "faculty1", 1.64),

        ("faculty2", "faculty1", 4.47),

        ("faculty2", "faculty3", 2.09),

        ("faculty4", "faculty3", 4.12),

        ("faculty4", "faculty5", 1.82),

        ("faculty12", "faculty13", 1.39),

        ("faculty12", "faculty11", 4.27),

        ("faculty10", "faculty11", 1.43),

        ("faculty10", "faculty9", 4.56),

        ("faculty14", "faculty9", 1.72),

        ("faculty13", "room12", 7.71),

        ("faculty5", "room12", 7.84),

        ("faculty7", "faculty8", 2.94),

        ("faculty7", "faculty6", 4.66),

        ("faculty15", "faculty16", 3.09),

        ("faculty14", "faculty15", 3.94),

        ("toilet1", "toilet2", 1),

        ("toilet4", "toilet3", 1),

        ("lift5", "lift6", 2),

        ("lift7", "lift8", 2),

        ("lift_lobby1", "lift6", 2),

        ("lift_lobby2", "lift8", 2),

        ("lift_lobby1", "lift5", 2),

        ("lift_lobby2", "lift7", 2), 

        ("meet1", "room1", 6.88),

        ("room10", "room1", 2.53),

        ("meet1", "faculty11", 2.81),

        ("meet1", "faculty15", 3.94),

        ("meet2", "room3", 8.4),

        ("room11", "room3", 3),

        ("lift6", "room11", 14),

        ("faculty7", "meet2", 5),

        ("faculty3", "meet2", 4.3),

        ("faculty8", "toilet2", 14.02),

        ("lab7", "ahu8", 5.94),

        ("lab9", "ahu8", 5.94),

        ("lab4", "ahu5", 11.64),

        ("lab6", "ahu5", 11.13),

        ("lab3", "ahu6", 6.89),

        ("lab5", "ahu6", 6.89),

        ("lab3", "lab4", 9.17),

        ("lab6", "lab5", 8.39),

        ("room8", "room9", 3.02),

        ("room8", "lift1", 10.7),

        ("lift2", "lift1", 2),

        ("lift_lobby3", "lift1", 2),

        ("lift_lobby3", "lift2", 2),

        ("lift_lobby3", "room4", 11.81),

        ("class2", "room4", 5.26),

        ("toilet5", "toilet6", 1),

        ("room4", "toilet6", 8.59),

        ("toilet6", "class2", 9.13),

        ("toilet8", "room5", 7.85),

        ("lab6", "lift_lobby3", 3.96),

        ("lab4", "lift_lobby1", 4.06),

        ("lab8", "lift_lobby2", 2.84),

        ("lab10", "lift_lobby4", 5.03),

        ("faculty16", "toilet4", 12.19),                                  

        ("room2", "ahu9", 4.21),

        ("room2", "faculty13", 6.90),

        ("lab2", "ahu4", 1.5),

        ("lab2", "ahu3", 4.94),

        ("room9", "ahu1", 6.72),

        ("room7", "ahu3", 3.92),

        ("stair2","lab4",7),

        ("stair2","room11",7.2),

        ("stair1","lab8",8.25),

        ("stair1","room10",10),

        ("stair4","lab10",7.2),

        ("stair4","room5",11.3),

        ("stair3","lab6",7.9),

        ("stair3","room4",11),

        
]

add_nodes_edges(G, floor3_nodes, floor3_edges)

rename_map_floor3 = {
      "faculty6": "11AC3021",
    "faculty1": "11AC3022",
    "faculty2": "11AC3023",
    "faculty7": "11AC3020",
    "faculty8": "11AC3019",
    "faculty3": "11AC3024",
    "faculty4": "11AC3025",
    "faculty5": "11AC3026",
    "faculty13": "11AC3031",
    "faculty12": "11AC3032",
    "faculty11": "11AC3033",
    "faculty10": "11AC3034",
    "faculty9": "11AC3035",
    "faculty14": "11AC3036",
    "faculty15": "11AC3037",
    "faculty16": "11AC3038",
    "room12":"11AC3027",
    "store1":"11AC3028",
    "ahu9":"11AC3029",
    "room2":"11AC3030",
    "meet1":"11AC3042",
    "room1":"11AC3041",
    "room10":"11AC3040",
    "lab8":"11AC3044",
    "lab7":"11AC3043",
    "lab10":"11AC3046",
    "lab9":"11AC3047",
    "ahu7":"11AC3045",
    "ahu8":"11AC3048",
    "lab3":"11AC3014",
    "lab4":"11AC3013",
    "lab5":"11AC3009",
    "lab6":"11AC3011",
    "ahu5":"11AC3012",
    "ahu6":"11AC3010",
    "room6":"11AC3050",
    "room7":"11AC3049",
    "room5":"11AC3051",
    "ahu3":"11AC3054",
    "ahu4":"11AC3056",
    "ahu1":"11AC3003",
    "ahu2":"11AC3002",
    "lab1":"11AC3001",
    "lab2":"11AC3055",
    "class2":"11AC3004",
    "class1":"11AC3005",
    "class4":"11AC3053",
    "class3":"11AC3052",
    "room8":"11AC3007",
    "room9":"11AC3008",
    "room4":"11AC3006",
    "room3":"11AC3016",
    "room11":"11AC3017",
    "meet2":"11AC3015",
    "lift1":"f3lift1","lift2":"f3lift2","lift3":"f3lift3","lift4":"f3lift4","lift5":"f3lift5","lift6":"f3lift6","lift7":"f3lift7","lift8":"f3lift8",
    "stair1":"f3stair1","stair2":"f3stair2","stair3":"f3stair3","stair4":"f3stair4",

}
rename_graph_nodes(G, rename_map_floor3)

# Floor 4
floor4_nodes = extract_nodes(dxf_f4)
floor4_edges = [
      ("class1", "ahu1", 9.3 ), ("ahu1", "class3", 9.74), ("class3", "class2", 12.53),("class4","class3",12.5),

        ("toilet5", "toilet6", 1), ("lab1", "ahu8", 19.2), ("lab2", "lab3",11.5), ("lab3", "ahu7", 14.2),

        ("class4", "ahu3", 13), ("ahu3", "ahu4", 1), ("ahu3", "class6", 4), ("class6", "class5", 11),

        ("toilet7", "toilet8", 1), ("lift4", "lift3", 2), ("entrance_lobby1", "cafe1", 14),

        ("entrance_lobby1", "faculty1", 15), ("toilet1", "toilet2", 1), ("toilet3", "toilet4", 1),

        ("faculty1", "room6", 16), ("lab5", "lab4", 8), ("ahu9", "lab4", 11), ("ahu9", "lab5", 12),

        ("ahu9", "lab7", 14), ("lab7", "lab8", 12.2), ("lab6", "ahu8", 1),        ("stair3", "lab1", 6),

        ("lab6", "lab1", 3), ("ahu7", "lab1", 12.46), ("ahu7", "lab3", 11), ("lift6", "lift_lobby1", 2),

        ("lift5", "lift_lobby1", 2), ("lift7", "lift_lobby2", 2), ("lift8", "lift_lobby2", 2),

        ("lift7", "lift8", 2), ("lift5", "lift6", 2), ("faculty1", "room1", 10.5), ("ahu5", "room1", 5.3),

        ("toilet2", "room1", 16), ("toilet3", "room4", 16), ("cafe1", "room4", 11),("stair1","ahu9",9.5),

        ("cafe1", "room7", 14), ("room4", "room7", 12), ("lift_lobby2", "room7", 10),("lab3","stair2",5.5),("stair2","toilet2",12),

        ("lift_lobby2", "lab5", 2), ("toilet4", "lab5", 3), ("lift2", "lift1", 2),

        ("lift_lobby3", "lift1", 2), ("lift_lobby3", "lift2", 2), ("room11", "room10", 4.78),

        ("lift_lobby3", "room10", 14.67), ("room2", "room10", 4.85), ("room2", "toilet6", 9.86),

        ("room3", "toilet8", 10), ("room8", "room9", 3.37), ("room8", "lift_lobby4", 11.3), ("stair1", "lab5", 5.5), 

        ("lift3", "lift_lobby4", 2), ("lift4", "lift_lobby4", 2), ("lab1", "lift_lobby3", 6), ("stair3", "lift_lobby3", 2), ("stair4", "lift_lobby4", 2), 

        ("lab7", "lift_lobby4", 4), ("lab3", "lift_lobby1", 4), ("room3", "room8", 2), ("room2", "stair3", 4),("room3", "stair4",4),("lab7", "stair4",7),

        ("room11", "class1", 17), ("room9", "class4", 16), 

        ("class4", "class1", 3),("scholar1","scholar2",11),("scholar3","scholar4",3.5),("room4","scholar4",11),("room1","scholar1",3),("scholar4","scholar3",11)
]
add_nodes_edges(G, floor4_nodes, floor4_edges)

rename_map_floor4 = {
    "scholar1": "11AC4020", "scholar2": "11AC4021", "scholar3": "11AC4023", "scholar4": "11AC4022",
        "ahu5": "11AC4019", "faculty1": "11AC4015", "ahu8": "11AC4010", "lab2": "11AC4014",
        "lab3": "11AC4013", "lab6": "11AC4009", "lab1": "11AC4011", "ahu7": "11AC4012",
        "room2": "11AC4006", "room10": "11AC4007", "room11": "11AC4008", "ahu1": "11AC4003",
        "ahu2": "11AC4002", "class1": "11AC4001", "class2": "11AC4005", "class3": "11AC4004",
        "room6": "11AC4016", "cafe": "11AC4028", "room7": "11AC4027", "lab5": "11AC4030",
        "lab4": "11AC4029", "ahu10": "11AC4034", "ahu9": "11AC4031", "lab7": "11AC4032",
        "lab8": "11AC4033", "room8": "11AC4036", "room9": "11AC4035", "room3": "11AC4037",
        "class5": "11AC4038", "class6": "11AC4039", "ahu3": "11AC4040", "ahu4": "11AC4042",
        "class4": "11AC4041","room1":"11AC4018","room4":"11AC4025","lift1":"f4lift1","lift2":"f4lift2","lift3":"f4lift3","lift4":"f4lift4","lift5":"f4lift5","lift6":"f4lift6","lift7":"f4lift7","lift8":"f4lift8",
        "stair1":"f4stair1","stair2":"f4stair2","stair3":"f4stair3","stair4":"f4stair4",
}
rename_graph_nodes(G, rename_map_floor4)


# Inter-floor connections (using renamed names directly)
inter_floor_edges = [
    ("f0stair1", "f1stair1", 22),
    ("f0stair2", "f1stair2", 22),
     ("f1stair1", "f2stair2", 22),
    ("f1stair2", "f2stair3", 22),
    ("f3stair3", "f2stair2", 22),
    ("f3stair4", "f2stair3", 22),
     ("f3stair3", "f4stair3", 22),
    ("f3stair4", "f4stair4", 22),
    ("f2stair4","f3stair2",22),
    ("f2stair1","f3stair1",22),
    ("f4stair2","f3stair2",22),
    ("f4stair1","f3stair1",22),
    ("f0lift1","f1lift1",36),
     ("f0lift2","f1lift2",36),
      ("f0lift3","f1lift3",36),
    ("f0lift4","f1lift4",36),
    ("f1lift1","f2lift1",36),
    ("f1lift2","f2lift2",36),
    ("f1lift3","f2lift3",36),
    ("f1lift4","f2lift4",36),
     ("f2lift1","f3lift1",36),
       ("f2lift2","f3lift2",36),
         ("f2lift3","f3lift3",36),
           ("f2lift4","f3lift4",36),
       ("f3lift1","f4lift1",36),
         ("f3lift2","f4lift2",36),
           ("f3lift3","f4lift3",36),
             ("f3lift4","f4lift4",36),
  ("f2lift6","f3lift6",36),
   ("f2lift5","f3lift5",36),
    ("f2lift7","f3lift7",36),
     ("f2lift8","f3lift8",36),
 ("f4lift6","f3lift6",36),
   ("f4lift5","f3lift5",36),
    ("f4lift7","f3lift7",36),
     ("f4lift8","f3lift8",36),
  ("f0stair_up3","f1stair_up1",16.52),
  ("f0stair_up5","f1stair_up1",16.52),
  ("f0stair_up6","f1stair_up1",16.52),
  ("f1stair_up1","f2stair_up3",28.18),
  ("f1stair_up1","f2stair_up6",28.18),
  ("f1stair_up1","f2stair_up5",28.18),
  ("f0lift1","f2lift1",38),
  ("f0lift2","f2lift2",38),
  ("f0lift3","f2lift3",38),
  ("f0lift4","f2lift4",38),
  ("f0lift1","f3lift1",40),
  ("f0lift2","f3lift2",40),
  ("f0lift3","f3lift3",40),
  ("f0lift4","f3lift4",40),
  ("f0lift1","f4lift1",45),
  ("f0lift2","f4lift2",45),
  ("f0lift3","f4lift3",45),
  ("f0lift4","f4lift4",45),
  ("f1lift1","f4lift1",40),
  ("f1lift2","f4lift2",40),
  ("f1lift3","f4lift3",40),
  ("f1lift4","f4lift4",40),
  ("f2lift1","f4lift1",38),
  ("f2lift2","f4lift2",38),
  ("f2lift3","f4lift3",38),
  ("f2lift4","f4lift4",38),
  ("f1lift1","f3lift1",38),
  ("f1lift2","f3lift2",38),
  ("f1lift3","f3lift3",38),
  ("f1lift4","f3lift4",38),
  ("f2lift5","f4lift5",38),
  ("f2lift6","f4lift6",38),
  ("f2lift7","f4lift7",38),
  ("f2lift8","f4lift8",38),
       
    
]

G.add_weighted_edges_from(inter_floor_edges)

# Optional: Visualize
# def draw_graph(G):
#     pos = nx.get_node_attributes(G, 'pos')
#     weights = nx.get_edge_attributes(G, 'weight')
#     nx.draw(G, pos, with_labels=True, node_size=500, font_size=8, width=list(weights.values()))
  

# draw_graph(G)

import heapq

# Custom Dijkstra's Algorithm
def dijkstra(graph, s, d):
    dist = {node: float('inf') for node in graph}
    dist[s] = 0
    prev = {node: None for node in graph}
    pq = [(0, s)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        if u == d:
            break

        if current_dist > dist[u]:
            continue

        for neighbor, weight in graph[u]:
            alt = dist[u] + weight
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = u
                heapq.heappush(pq, (alt, neighbor))

    path = []
    u = d
    while u is not None:
        path.append(u)
        u = prev[u]
    path.reverse()

    if dist[d] == float('inf'):
        return None, float('inf')
    return path, dist[d]

# Convert NetworkX graph to adjacency list
def nx_to_adjlist(G):
    adj = {}
    for u in G.nodes():
        adj[u] = []
        for v in G.neighbors(u):
            weight = G[u][v].get("weight", 1)
            adj[u].append((v, weight))
    return adj

# Get adjacency list
adj_list = nx_to_adjlist(G)

# # Choose your start and end nodes here:
# start_node = sys.argv[1]
# end_node = sys.argv[2]
# # start_node = input("Enter start node: ")
# # end_node = input("Enter end node: ")

# if start_node in adj_list and end_node in adj_list:
#     path, total_distance = dijkstra(adj_list, start_node, end_node)
#     if path:
#         result = f"Shortest path: {' -> '.join(path)}\nTotal time taken: {total_distance} seconds"
#         print(result)
#     else:
#         result = f"No path found from {start_node} to {end_node}"
#         print(result)
# else:
#     result = "Start or end node not found in graph."
#     print(result)



from flask import Flask, request, jsonify, send_from_directory
import os

from flask_cors import CORS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "../frontend")

app = Flask(
    __name__,
    static_folder=FRONTEND_DIR,
    static_url_path=""
)

CORS(app)

@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)


@app.route("/shortest-path")
def shortest_path():
    start = request.args.get("start", "").strip().upper()
    end = request.args.get("end", "").strip().upper()

    if not start or not end:
        return jsonify({"error": "start and end required"}), 400

    if start not in adj_list or end not in adj_list:
        return jsonify({"error": "Invalid node"}), 400

    path, dist = dijkstra(adj_list, start, end)

    if not path:
        return jsonify({"error": "No path found"}), 404

    return jsonify({
        "path": path,
        "time": dist
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# from flask import Flask, request, jsonify, send_from_directory
# import os
# from flask_cors import CORS


# app = Flask(__name__, static_folder="frontend")
# CORS(app)

# @app.route("/")
# def serve_frontend():
#     return send_from_directory(app.static_folder, "index.html")

# @app.route("/<path:path>")
# def serve_static_files(path):
#     return send_from_directory(app.static_folder, path)


# # @app.route("/")
# # def home():
# #     return "i-Nav backend running 🚀"

# @app.route("/compute", methods=["POST"])
# def compute():
#     data = request.get_json()
#     start_node = data.get("start")
#     end_node = data.get("end")

#     if not start_node or not end_node:
#         return jsonify({"error": "start and end required"}), 400

#     if start_node not in adj_list or end_node not in adj_list:
#         return jsonify({"error": "Invalid node"}), 400

#     path, total_distance = dijkstra(adj_list, start_node, end_node)

#     return jsonify({
#         "path": path,
#         "total_time": total_distance
#     })

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host="0.0.0.0", port=port)



