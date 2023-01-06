# https://leetcode.com/problems/max-points-on-a-line

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        frequencies = {}
        maxpoints = 0
        for i in range(0, len(points)):
            for j in range(i+1, len(points)):
                if points[j][0] - points[i][0] == 0: # denominator = 0 , slope is maximum
                    slope = 100000001
                else:
                    slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])            
                frequencies[slope] = 1 if slope not in frequencies else frequencies.get(slope) + 1
                maxpoints = max(maxpoints, frequencies[slope])
            frequencies.clear()
        return maxpoints + 1