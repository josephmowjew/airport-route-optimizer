from graph import DirectedGraph

def test_airport_routes():
    # Initialize graph
    airport_graph = DirectedGraph()
    
    # Add routes from the diagram
    routes = [
        ("DSM", "ORD"), ("ORD", "BGI"), ("BGI", "LGA"), ("JFK", "LGA"),
        ("JFK", "ICN"), ("HND", "ICN"), ("EWR", "HND"), ("TLV", "DEL"),
        ("DEL", "DOH"), ("DEL", "CDG"), ("CDG", "BUD"), ("CDG", "SIN"),
        ("SFO", "SAN"), ("SFO", "DSM"), ("EYW", "LHR"), ("LHR", "SFO"),
        ("EYW", "SAN")
    ]
    
    # Add all routes to graph
    for origin, destination in routes:
        airport_graph.add_edge(origin, destination)
    
    # Test connectivity from SFO
    start_airport = "SFO"
    stats = airport_graph.calculate_connectivity_stats(start_airport)
    
    # Print results
    print(f"\nAirport Connectivity Analysis from {start_airport}")
    print("="*50)
    print(f"Total Airports: {stats['total_vertices']}")
    print(f"Total Routes: {stats['total_edges']}")
    print(f"Reachable Airports: {stats['reachable_count']}")
    print(f"Unreachable Airports: {stats['unreachable_count']}")
    print(f"\nMinimum Additional Routes Needed: {airport_graph.min_additional_routes(start_airport)}")
    print("\nCurrently Reachable Airports:")
    print(", ".join(stats['reachable_vertices']))
    print("\nCurrently Unreachable Airports:")
    print(", ".join(stats['unreachable_vertices']))

if __name__ == "__main__":
    test_airport_routes()