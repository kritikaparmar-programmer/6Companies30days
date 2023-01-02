# https://leetcode.com/problems/largest-divisible-subset/description/

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [1] * n 
        hash = [i for i in range(n)]
        maxi = 1
        lastInd = 0
        nums.sort() # sorting the array
        for ind in range(n):
            for prevInd in range(ind):

                if nums[ind] % nums[prevInd] == 0 and (1 + dp[prevInd] > dp[ind])    :
                    dp[ind] = 1 + dp[prevInd]
                    hash[ind] = prevInd
        
            if dp[ind] > maxi:
                maxi = dp[ind]
                lastInd = ind
                
        lis = []
        lis.append(nums[lastInd])
        while hash[lastInd] != lastInd:
            lastInd = hash[lastInd]
            lis.append(nums[lastInd])
        
        return list(reversed(lis))