# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

import heapq
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        def calc(l, r, u, d):
            sums = 0
            c1 = c2 = (l+r) // 2
            expand = True  # flag
            for row in range(u, d+1):
                if c1 == c2:
                    sums += grid[row][c1]
                else:
                    sums += grid[row][c1] + grid[row][c2]

                if c1 == l: # c1 reach border
                    expand = False
                
                if expand:
                    c1 -= 1
                    c2 += 1
                else:
                    c1 += 1
                    c2 -= 1
            return sums

        pq = []
        for i in range(m):
            for j in range(n):
                left = right = j
                down = i
                while left >= 0 and right < n and down < m:
                    sumOfRhombus = calc(left, right, i, down)
                    left -= 1
                    right += 1
                    down += 2 # to make rhombus

                    if len(pq) < 3:
                        if sumOfRhombus not in pq:  # to get distinct vals
                            heapq.heappush(pq, sumOfRhombus)
                    else:
                        if sumOfRhombus not in pq and sumOfRhombus > pq[0]:
                            heapq.heappop(pq)
                            heapq.heappush(pq, sumOfRhombus)
    
        pq.sort(reverse = True)
        return pq