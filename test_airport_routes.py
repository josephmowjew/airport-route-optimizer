# test_airport_routes.py

from graph import DirectedGraph

def test_airport_routes():
    # Initialize graph
    graph = DirectedGraph()
    
    # Add routes from the diagram
    routes = [
        ("DSM", "ORD"), ("ORD", "BGI"), ("BGI", "LGA"), ("LGA", "DSM"),  # Cycle 1
        ("JFK", "ICN"), ("ICN", "HND"), ("HND", "EWR"), ("EWR", "JFK"),  # Cycle 2
        ("TLV", "DEL"), ("DEL", "DOH"), ("DOH", "CDG"), ("CDG", "BUD"), 
        ("BUD", "TLV"), ("CDG", "SIN"), ("SIN", "TLV"),  # Cycle 3
        ("SFO", "SAN"), ("SFO", "DSM"), ("EYW", "LHR"), ("LHR", "EYW"),  # Cycle 4
        ("SAN", "SFO")  # Make SFO-SAN a cycle
    ]
    
    # Add all routes to graph
    for origin, destination in routes:
        graph.add_edge(origin, destination)
    
    # Find SCCs
    sccs = graph.find_strongly_connected_components()
    
    # Start airport
    start_airport = "SFO"
    
    print("\nAirport Route Analysis")
    print("=====================")
    
    # Print SCCs
    print("\nStrongly Connected Components:")
    for i, scc in enumerate(sccs):
        print(f"Component {i}: {', '.join(scc)}")
    
    # Get compressed graph
    compressed_graph, vertex_to_scc = graph.compress_graph(sccs)
    
    # Calculate minimum additional routes
    min_routes = graph.min_additional_routes(start_airport)
    
    print(f"\nStart Airport: {start_airport}")
    print(f"Minimum Additional Routes Needed: {min_routes}")

if __name__ == "__main__":
    test_airport_routes()
