

from data_structures import Stack, Queue

class DirectedGraph:
    """Custom implementation of a directed graph using adjacency list"""
    def __init__(self):
        self.adjacency_list = {}
        self.vertex_count = 0
        self.edge_count = 0
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph"""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            self.vertex_count += 1
    
    def add_edge(self, from_vertex, to_vertex):
        """Add a directed edge from one vertex to another"""
        # Add vertices if they don't exist
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        
        # Add edge if it doesn't exist
        if to_vertex not in self.adjacency_list[from_vertex]:
            self.adjacency_list[from_vertex].append(to_vertex)
            self.edge_count += 1
    
    def get_vertices(self):
        """Return list of all vertices in the graph"""
        return list(self.adjacency_list.keys())
    
    def get_neighbors(self, vertex):
        """Return list of all neighbors of a vertex"""
        return self.adjacency_list.get(vertex, [])
    
    def dfs_reachable(self, start):
        """
        Custom Depth-First Search implementation to find all reachable vertices
        Returns a set of vertices reachable from start vertex
        """
        if start not in self.adjacency_list:
            return set()
        
        visited = set()
        stack = Stack()
        stack.push(start)
        
        while not stack.is_empty():
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                # Push unvisited neighbors onto stack
                for neighbor in reversed(self.get_neighbors(vertex)):
                    if neighbor not in visited:
                        stack.push(neighbor)
        
        return visited
    
    def bfs_reachable(self, start):
        """
        Custom Breadth-First Search implementation to find all reachable vertices
        Returns a set of vertices reachable from start vertex
        """
        if start not in self.adjacency_list:
            return set()
        
        visited = set()
        queue = Queue()
        queue.enqueue(start)
        visited.add(start)
        
        while not queue.is_empty():
            vertex = queue.dequeue()
            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)
        
        return visited
    
    def min_additional_routes(self, start):
        """
        Calculate minimum number of additional routes needed
        to make all vertices reachable from start vertex
        """
        # Get currently reachable vertices using DFS
        reachable = self.dfs_reachable(start)
        
        # Find unreachable vertices
        unreachable = set(self.get_vertices()) - reachable
        
        # For optimal solution, we need one new route to each unreachable vertex
        return len(unreachable)
    
    def get_unreachable_vertices(self, start):
        """Return list of vertices that are not reachable from start vertex"""
        reachable = self.dfs_reachable(start)
        return [v for v in self.get_vertices() if v not in reachable]

    def calculate_connectivity_stats(self, start):
        """
        Calculate and return detailed connectivity statistics
        """
        reachable = self.dfs_reachable(start)
        unreachable = set(self.get_vertices()) - reachable
        
        return {
            'total_vertices': self.vertex_count,
            'total_edges': self.edge_count,
            'reachable_count': len(reachable),
            'unreachable_count': len(unreachable),
            'reachable_vertices': sorted(list(reachable)),
            'unreachable_vertices': sorted(list(unreachable))
        }