# https://leetcode.com/problems/maximum-points-in-an-archery-competition/
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        dp = [[-1 for _ in range(numArrows + 1)] for _ in range(12)]
        minArrowsForBobToWin = [0] * 12
        for i in range(len(aliceArrows)):
            minArrowsForBobToWin[i] = aliceArrows[i] + 1
        bobMaxScore = [0] * 12
        
        def findMaxScore(section, numArrows):
            if numArrows <= 0 or section <= 0:
                return 0
            if dp[section][numArrows] != -1:
                return dp[section][numArrows]
            taken, notTaken = 0, 0
            if numArrows >= minArrowsForBobToWin[section]:
                taken =  section + findMaxScore(section - 1, numArrows - minArrowsForBobToWin[section])
            notTaken = findMaxScore(section - 1, numArrows)
            dp[section][numArrows] = max(taken, notTaken)
            return dp[section][numArrows]
        
        findMaxScore(11, numArrows)
        for i in range(11, 0, -1):
            if numArrows >= minArrowsForBobToWin[i] and dp[i][numArrows] > dp[i - 1][numArrows]:
                bobMaxScore[i] = minArrowsForBobToWin[i]
                numArrows -= minArrowsForBobToWin[i]
                if numArrows <= 0:
                    break
        if numArrows > 0: # add remaining arrows in section 0
            bobMaxScore[0] = numArrows
        return bobMaxScore