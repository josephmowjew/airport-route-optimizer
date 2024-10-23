# Airport Route Optimizer

## Overview
Airport Route Optimizer analyzes airport networks using Strongly Connected Components (SCCs) to determine the minimum number of additional routes needed for full connectivity from a starting airport.

## Problem Statement
Given a network of airports and existing one-way flight routes, determine the minimum number of additional one-way routes needed to make all airports reachable from a designated starting airport.

## Technical Implementation
The solution uses three key components:

1. **Graph Implementation** (`graph.py`)
   - Directed graph with adjacency list representation
   - Kosaraju's algorithm for finding SCCs
   - Graph compression for SCC-based analysis
   - Minimum additional routes calculator

2. **Data Structures** (`data_structures.py`)
   - Queue implementation
   - Stack implementation

3. **Testing** (`test_airport_routes.py`)
   - Network analysis and visualization
   - Sample route testing

## Algorithm Details
The solution uses a two-phase approach:
1. Find Strongly Connected Components using Kosaraju's Algorithm
2. Compress the graph by converting SCCs to single nodes
3. Count nodes with zero in-degree (excluding start node's SCC)

- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)

## Usage
```bash
python test_airport_routes.py
```

### Example Output
```
Airport Route Analysis
=====================

Strongly Connected Components:
Component 0: SFO, DSM, ORD, BGI, LGA
Component 1: JFK, ICN, HND, EWR
Component 2: TLV, DEL, DOH, CDG, BUD, SIN
Component 3: EYW, LHR
Component 4: SAN

Start Airport: SFO
Minimum Additional Routes Needed: 4
```

## Project Structure
```
airport-route-optimizer/
├── README.md
├── data_structures.py
├── graph.py
└── test_airport_routes.py
```

## Installation
No external dependencies required - uses Python standard library only.

## Future Enhancements
- Route cost optimization
- Multiple starting points
- Network visualization
- Real-time route updates
- Route capacity constraints

## Author
Joseph Mojoo

## Acknowledgments
- Original problem inspired by real-world airline route optimization challenges
- Graph theory principles and algorithms

---
For more information or to report issues, please visit the [project repository](https://github.com/josephmowjew/airport-route-optimizer.git).
