# Problem Statement:
# You are given an undirected graph represented as an adjacency list or an edge list. 
# Some nodes in the graph are faulty and cannot be visited unless repaired. 
# You need to determine whether there exists a path from node A to node B while avoiding faulty nodes. Additionally, you need to answer the following variations of the problem:

# Reachability Check: Can you reach node B from node A without visiting any faulty nodes?
# Minimum Cost Path: If moving between two connected, non-faulty nodes has a cost of 1, 
# what is the minimum cost to reach B from A, if possible?
# Repair with Different Costs: If a faulty node can be repaired at a given cost 
# 𝐶
# [
# 𝑖
# ]
# C[i] (different for each faulty node), what is the minimum cost to reach B from A, considering both movement and repair costs?
# Repair with Uniform Cost: If all faulty nodes have the same repair cost 
# 𝐶
# C, what is the minimum cost to reach B from A, considering both movement and repair costs?
# Input Format:
# Graph Representation:

# 𝑛
# n (Number of nodes, 0-indexed or 1-indexed)
# 𝑚
# m (Number of edges)
# edges
# edges (List of edges, where each edge is 
# [
# 𝑢
# ,
# 𝑣
# ]
# [u,v] indicating an undirected connection)
# Faulty Nodes:

# 𝑓
# f (Number of faulty nodes)
# faulty_nodes
# faulty_nodes (List of faulty node indices)

# Explanation of Input Sections
# Graph Definition

# 7 nodes, 6 edges.
# Edges: (0-1), (1-2), (2-3), (3-4), (4-5), (5-6).
# Faulty Nodes

# 3 faulty nodes: {2, 4, 6}.
# Queries

# Query 1: 0 6 → Can we reach from node 0 to 6 avoiding faulty nodes?
# Query 2: 0 6 → What is the minimum cost to travel from 0 to 6 if each move costs 1?
# Query 3: 0 6 2 3 5 → What is the minimum cost if we can repair node 2 (cost = 2), node 4 (cost = 3), node 6 (cost = 5)?
# Query 4: 0 6 2 → What is the minimum cost if we can repair any faulty node for a uniform cost of 2?

from collections import deque, defaultdict
from heapq import heappush, heappop
import math

class GraphPathFinder:
    def __init__(self, edges, faulty_nodes):
        """
        Initialize the graph with edges and faulty nodes.
        
        Args:
            edges: List of tuples (node1, node2) representing undirected edges
            faulty_nodes: Set of nodes that are initially faulty
        """
        self.graph = defaultdict(list)
        self.faulty_nodes = set(faulty_nodes)
        
        # Build adjacency list
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
    
    def can_reach(self, start, end):
        """
        Problem 1: Check if it's possible to reach from start to end avoiding faulty nodes.
        Using BFS for shortest path in unweighted graph.
        """
        if start in self.faulty_nodes or end in self.faulty_nodes:
            return False
            
        visited = set([start])
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            if node == end:
                return True
                
            for neighbor in self.graph[node]:
                if neighbor not in visited and neighbor not in self.faulty_nodes:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return False
    
    def min_cost_path(self, start, end):
        """
        Problem 2: Find minimum cost path where each teleportation costs 1.
        Using Dijkstra's algorithm since all edges have same weight.
        """
        if start in self.faulty_nodes or end in self.faulty_nodes:
            return float('inf')
            
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        pq = [(0, start)]
        visited = set()
        
        while pq:
            dist, node = heappop(pq)
            
            if node == end:
                return dist
                
            if node in visited:
                continue
                
            visited.add(node)
            
            for neighbor in self.graph[node]:
                if neighbor not in self.faulty_nodes:
                    new_dist = dist + 1
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heappush(pq, (new_dist, neighbor))
        
        return float('inf')
    
    def min_cost_with_repairs(self, start, end, repair_costs):
        """
        Problem 3: Find minimum cost path with different repair costs for each node.
        Using modified Dijkstra's algorithm to handle repair decisions.
        
        Args:
            repair_costs: Dictionary mapping faulty nodes to their repair costs
        """
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        pq = [(0, start, frozenset())]  # (cost, node, repaired_nodes)
        
        while pq:
            cost, node, repaired = heappop(pq)
            
            if node == end:
                return cost
            
            for neighbor in self.graph[node]:
                if neighbor in self.faulty_nodes and neighbor not in repaired:
                    # Try repairing the node
                    new_repaired = set(repaired)
                    new_repaired.add(neighbor)
                    new_cost = cost + repair_costs[neighbor] + 1
                    heappush(pq, (new_cost, neighbor, frozenset(new_repaired)))
                elif neighbor not in self.faulty_nodes or neighbor in repaired:
                    # Node is either good or already repaired
                    new_cost = cost + 1
                    heappush(pq, (new_cost, neighbor, repaired))
        
        return float('inf')
    
    def min_cost_uniform_repairs(self, start, end, repair_cost):
        """
        Problem 4: Find minimum cost path with uniform repair cost.
        Using modified BFS with repair cost optimization.
        """
        if start == end:
            return 0
            
        visited = set()
        pq = [(0, start, frozenset())]  # (cost, node, repaired_nodes)
        
        while pq:
            cost, node, repaired = heappop(pq)
            
            if node == end:
                return cost
                
            state = (node, repaired)
            if state in visited:
                continue
            visited.add(state)
            
            for neighbor in self.graph[node]:
                if neighbor in self.faulty_nodes and neighbor not in repaired:
                    # Try repairing the node
                    new_repaired = set(repaired)
                    new_repaired.add(neighbor)
                    heappush(pq, (cost + repair_cost + 1, neighbor, frozenset(new_repaired)))
                elif neighbor not in self.faulty_nodes or neighbor in repaired:
                    # Node is either good or already repaired
                    heappush(pq, (cost + 1, neighbor, repaired))
        
        return float('inf')

# Example usage
def test_graph_solutions():
    # Create a sample graph
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 4),
        (0, 5), (5, 6), (6, 4),
        (1, 7), (7, 3)
    ]
    faulty_nodes = {2, 6}
    
    # Initialize solver
    solver = GraphPathFinder(edges, faulty_nodes)
    
    # Test Problem 1: Can reach?
    print("Can reach from 0 to 4:", solver.can_reach(0, 4))
    
    # Test Problem 2: Minimum cost path
    print("Minimum cost path from 0 to 4:", solver.min_cost_path(0, 4))
    
    # Test Problem 3: Variable repair costs
    repair_costs = {2: 3, 6: 2}  # Node 2 costs 3 to repair, node 6 costs 2
    print("Minimum cost with variable repairs:", 
          solver.min_cost_with_repairs(0, 4, repair_costs))
    
    # Test Problem 4: Uniform repair cost
    uniform_cost = 2
    print("Minimum cost with uniform repairs:", 
          solver.min_cost_uniform_repairs(0, 4, uniform_cost))

if __name__ == "__main__":
    test_graph_solutions()