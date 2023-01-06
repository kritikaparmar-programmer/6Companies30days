# https://leetcode.com/problems/valid-square/
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(point1, point2):
            return (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2
        
        dist = [
        dist(p1, p2), dist(p2, p3),
        dist(p3, p4), dist(p4, p1),
        dist(p1, p3), dist(p2, p4)
        ]
        # hashmap = {}
        # for d in dist:
        #     hashmap[d] = 1 if d not in hashmap else hashmap.get(d) + 1
       
        # if len(hashmap) > 2:
        #     return False
        
        # for i in hashmap:
        #     return hashmap[i] == 4 or hashmap[i] == 2

        # return False

        dist.sort()
        return 0<dist[0] == dist[1] == dist[2] == dist[3] and dist[4] == dist[5]