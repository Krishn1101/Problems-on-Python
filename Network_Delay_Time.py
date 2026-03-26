"""You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1"""

                                                    #CODE HERE:-

class Solution:
    def networkDelayTime(self,times,n,k):
        import heapq
        adjList = []
    
        for i in range(n):
            adjList.append([])
            
        for edge in times:
            x = edge[0]-1
            y = edge[1]-1
            w = edge[2]
            
            adjList[x].append([y,w])
        
        heap = []
        dist = [float("inf")]*n
        
        k-=1
        dist[k] = 0
        heapq.heappush(heap,(dist[k],k))
        
        while len(heap)>0:
            d,u = heapq.heappop(heap)
            for v,w in adjList[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap,(dist[v],v))
        
        ans = max(dist)
        if ans == float("inf"):
            return -1
        else:
            return ans