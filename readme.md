# Airport Route Optimizer

## Overview
Airport Route Optimizer is a Python-based solution that helps airlines optimize their flight routes by calculating the minimum number of additional routes needed to ensure all airports in a network are reachable from a starting point. The project implements custom graph algorithms and data structures to demonstrate a deep understanding of algorithmic problem-solving.

## Problem Statement
Given a network of airports and existing one-way flight routes, determine the minimum number of additional one-way routes needed to make all airports reachable from a designated starting airport.

## Features
- Custom implementation of fundamental data structures (Queue, Stack)
- Custom graph traversal algorithms (DFS, BFS)
- Route connectivity analysis
- Minimum additional routes calculator
- Detailed network statistics

## Technical Implementation
The project includes three main components:
1. **Custom Data Structures** (`data_structures.py`)
   - Queue implementation using linked list
   - Stack implementation using linked list

2. **Graph Implementation** (`graph.py`)
   - Directed graph representation using adjacency list
   - Custom DFS and BFS implementations
   - Route analysis algorithms

3. **Testing Module** (`test_airport_routes.py`)
   - Comprehensive test cases
   - Network analysis visualization

## Project Structure
```
airport-route-optimizer/
├── README.md
├── data_structures.py
├── graph.py
└── test_airport_routes.py
```

## Installation and Setup
1. Clone the repository:
```bash
git clone https://github.com/josephmowjew/airport-route-optimizer.git
cd airport-route-optimizer
```

2. No additional dependencies required - the project uses only Python standard library.

## Usage
Run the test script to analyze the airport network:
```bash
python test_airport_routes.py
```

### Example Output
```
Airport Connectivity Analysis from SFO
==================================================
Total Airports: 17
Total Routes: 17
Reachable Airports: 12
Unreachable Airports: 5
Minimum Additional Routes Needed: 5

Currently Reachable Airports:
BGI, BUD, CDG, DOH, DSM, LGA, ORD, SAN, SFO, SIN

Currently Unreachable Airports:
EWR, HND, ICN, JFK, TLV
```

## Algorithm Details
- **Time Complexity**: O(V + E) where V is the number of vertices (airports) and E is the number of edges (routes)
- **Space Complexity**: O(V) for storing visited nodes during traversal

## Contributing
1. Fork the repository
2. Create your feature branch: `git checkout -b feature/new-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/new-feature`
5. Submit a pull request

## Future Enhancements
- Add support for weighted edges (route costs/distances)
- Implement multiple starting points analysis
- Add visualization of the route network
- Include route optimization based on additional constraints
- Add support for bidirectional routes analysis

## License
[]

## Author
Joseph Mojoo

## Acknowledgments
- Original problem inspired by real-world airline route optimization challenges
- Graph theory principles and algorithms

---
For more information or to report issues, please visit the [project repository](https://github.com/josephmowjew/airport-route-optimizer.git).