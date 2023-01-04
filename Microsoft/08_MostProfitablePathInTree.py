# https://leetcode.com/problems/most-profitable-path-in-a-tree/description/

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount) 

        # creating adjacency list
        graph = {i:[] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        parent = [-1 for i in range(n)]
        dist = [0 for i in range(n)]

        def findDistancefromStart(cur, curParent):
            for it in graph[cur]:
                if it != curParent:
                    dist[it] = dist[cur] + 1
                    findDistancefromStart(it, cur)
                    parent[it] = cur

        def modifyAmount(curBob, curDist):
            while curBob != 0:
                if curDist < dist[curBob]: # current distance is less than the actual distance of bob from the start
                    amount[curBob] = 0
                elif curDist == dist[curBob]: 
                    amount[curBob] = amount[curBob] // 2
                curBob = parent[curBob]
                curDist += 1

        visited = set()
        cost = 0
        income = float('-inf')
        def findMaxProfitPath(cur):
            nonlocal cost
            nonlocal income
            visited.add(cur)
            cost += amount[cur]
            trav = 0 # to check if this is leaf node
            for it in graph[cur]:
                if it in visited:
                    continue
                trav += 1 # this shows that this is not a leaf node
                findMaxProfitPath(it)

            if trav == 0:
                income = max(cost, income)
            cost -= amount[cur]

        findDistancefromStart(0, -1)
        modifyAmount(bob, 0)
        findMaxProfitPath(0)

        return income