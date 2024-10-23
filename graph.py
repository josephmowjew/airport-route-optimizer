

class DirectedGraph:
    def __init__(self):
        self.adjacency_list = {}
        self.vertex_count = 0
        self.edge_count = 0
        
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            self.vertex_count += 1
    
    def add_edge(self, from_vertex, to_vertex):
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        if to_vertex not in self.adjacency_list[from_vertex]:
            self.adjacency_list[from_vertex].append(to_vertex)
            self.edge_count += 1

    def get_transpose(self):
        """
        Returns the transpose of the graph (all edges reversed)
        Used in Kosaraju's algorithm for finding SCCs
        """
        transpose = DirectedGraph()
        for vertex in self.adjacency_list:
            transpose.add_vertex(vertex)
            for neighbor in self.adjacency_list[vertex]:
                transpose.add_edge(neighbor, vertex)
        return transpose

    def _dfs_for_finish_time(self, vertex, visited, finish_order):
        """
        DFS utility function that stores vertices in order of finish time
        Used in first pass of Kosaraju's algorithm
        """
        visited.add(vertex)
        for neighbor in self.adjacency_list[vertex]:
            if neighbor not in visited:
                self._dfs_for_finish_time(neighbor, visited, finish_order)
        finish_order.append(vertex)

    def _dfs_for_scc(self, vertex, visited, scc):
        """
        DFS utility function that collects vertices in the same SCC
        Used in second pass of Kosaraju's algorithm
        """
        visited.add(vertex)
        scc.append(vertex)
        for neighbor in self.adjacency_list[vertex]:
            if neighbor not in visited:
                self._dfs_for_scc(neighbor, visited, scc)

    def find_strongly_connected_components(self):
        """
        Implements Kosaraju's algorithm to find strongly connected components
        
        Algorithm steps:
        1. Perform DFS on original graph to get finish times
        2. Create transpose of the graph
        3. Perform DFS on transpose in order of finish times
        
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        # Step 1: Get finish times using DFS
        visited = set()
        finish_order = []
        for vertex in self.adjacency_list:
            if vertex not in visited:
                self._dfs_for_finish_time(vertex, visited, finish_order)

        # Step 2: Get transpose graph
        transpose = self.get_transpose()

        # Step 3: DFS on transpose using finish times
        visited = set()
        sccs = []
        for vertex in reversed(finish_order):
            if vertex not in visited:
                current_scc = []
                transpose._dfs_for_scc(vertex, visited, current_scc)
                sccs.append(current_scc)

        return sccs

    def compress_graph(self, sccs):
        """
        Creates a compressed graph where each SCC becomes a single node
        Returns: (compressed graph, mapping of original vertices to SCC ids)
        """
        # Create mapping from vertex to its SCC ID
        vertex_to_scc = {}
        for i, scc in enumerate(sccs):
            for vertex in scc:
                vertex_to_scc[vertex] = i

        # Create compressed graph
        compressed = DirectedGraph()
        
        # Add edges between different SCCs
        for from_vertex in self.adjacency_list:
            from_scc = vertex_to_scc[from_vertex]
            for to_vertex in self.adjacency_list[from_vertex]:
                to_scc = vertex_to_scc[to_vertex]
                if from_scc != to_scc:  # Only add edge if SCCs are different
                    compressed.add_edge(from_scc, to_scc)

        return compressed, vertex_to_scc

    def count_zero_indegree(self, start_scc):
        """
        Counts nodes with in-degree = 0, excluding the start node's SCC
        """
        # Calculate in-degrees
        in_degrees = {vertex: 0 for vertex in self.adjacency_list}
        for vertex in self.adjacency_list:
            for neighbor in self.adjacency_list[vertex]:
                in_degrees[neighbor] += 1

        # Count vertices with in-degree 0, excluding start_scc
        count = 0
        for vertex, in_degree in in_degrees.items():
            if in_degree == 0 and vertex != start_scc:
                count += 1
                
        return count

    def min_additional_routes(self, start):
        """
        Calculate minimum additional routes needed using SCC-based approach
        
        Steps:
        1. Find SCCs
        2. Compress graph based on SCCs
        3. Count nodes with in_degree = 0 (excluding start node's SCC)
        """
        # Find SCCs
        sccs = self.find_strongly_connected_components()
        
        # Create compressed graph
        compressed_graph, vertex_to_scc = self.compress_graph(sccs)
        
        # Find SCC containing start vertex
        start_scc = vertex_to_scc[start]
        
        # Count zero in-degree nodes in compressed graph
        return compressed_graph.count_zero_indegree(start_scc)