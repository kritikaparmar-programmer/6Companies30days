# https://leetcode.com/problems/number-of-boomerangs/
class Solution:
    def numberOfBoomerangs(self, points) -> int:
        boomerangs = 0
        for point1 in points:
            freq = {} # separate map for every point
            for point2 in points:
                dis = (point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 
                freq[dis] = 1 if dis not in freq else freq[dis] + 1
            for k in freq:
                boomerangs += freq[k] * (freq[k] - 1)
        return boomerangs 