## i-Nav: Intelligent Indoor Navigation System


**Overview**
i-Nav is a smart indoor navigation system developed for IIT Jammu’s multi-floor Pushkar building. It computes the least-time path between rooms across multiple floors, considering real-world traversal factors like stairs, lifts, and corridor distances.

---

### Key Features

* **Fastest-Time Routing Algorithm**
  Implements a customized Dijkstra’s Algorithm on a weighted, multi-floor graph where edge weights represent real-time traversal durations rather than just distances.

* **Realistic Edge Cost Modeling**
  Edge weights are dynamically calculated based on:

  * Horizontal distances between nodes (e.g., corridors)
  * Vertical transitions via stairs or lifts with time penalties

* **Efficient Computation**

  * Utilizes priority queues (min-heaps) for efficient node selection
  * Achieves fast response times suitable for real-time indoor routing

* **DXF Floorplan Parsing**

  * Parses CAD-based `.dxf` files to extract nodes, room coordinates, and floor connections
  * Enables automated graph generation directly from architectural blueprints

* **Backend and API Integration**

  * Backend developed using Node.js and Express
  * RESTful API endpoints serve pathfinding results for easy frontend integration

---

### Tools & Technologies Used

* Python – Core graph logic and Dijkstra's implementation
* NetworkX – Graph representation and traversal
* DXF Parsing – CAD file extraction and processing
* Node.js & Express – Backend and API services
* Custom Graph Algorithms – Time-weighted, multi-floor pathfinding

---

### Impact & Use Case

This project enables efficient and realistic indoor navigation within complex buildings such as academic campuses, hospitals, and commercial facilities—where traversal time is more critical than physical distance.
