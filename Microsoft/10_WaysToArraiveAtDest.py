# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        heap = []
        heapq.heappush(heap, (0, 0))
        mod = int(1e9 + 7)

        while heap:
            dis, node = heapq.heappop(heap)

            for adj in graph[node]:
                adjNode = adj[0]
                adjW = adj[1]
                if dis + adjW < dist[adjNode]:
                    dist[adjNode] = dis + adjW
                    heapq.heappush(heap, (dist[adjNode], adjNode))
                    ways[adjNode] = ways[node]
                elif dis + adjW == dist[adjNode]:
                    ways[adjNode] += ways[node]
                
        return ways[n - 1] % mod