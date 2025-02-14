# Network Delay Time
# Solved 
# You are given a network of n directed nodes, labeled from 1 to n. You are also given times,
# a list of directed edges where times[i] = (ui, vi, ti).

# ui is the source node (an integer from 1 to n)
# vi is the target node (an integer from 1 to n)
# ti is the time it takes for a signal to travel from the source to the target node 
# (an integer greater than or equal to 0).
# You are also given an integer k, representing the node that we will send a signal from.

# Return the minimum time it takes for all of the n nodes to receive the signal. 
# If it is impossible for all the nodes to receive the signal, return -1 instead.

# Example 1:



# Input: times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1

# Output: 3
# Example 2:

# Input: times = [[1,2,1],[2,3,1]], n = 3, k = 2

# Output: -1

from collections import defaultdict
import heapq
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))
        visit = set()
        minHeap = [(0,k)]
        t = 0
        while minHeap:
            w1,n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            t = max(t,w1)
            visit.add(n1)
            for n2,w2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap,(w1+w2,n2))
        return t if len(visit) == n else -1

# Steps of Dijkstra’s Algorithm
# Initialize:

# Set the distance to the source as 0 and all other nodes as ∞ (infinity).
# Use a priority queue (min-heap) to process nodes with the smallest known distance.
# Process Nodes:

# Extract the node with the smallest distance.
# Update distances to its neighbors if a shorter path is found.
# Repeat Until All Nodes Are Processed.