# https://leetcode.com/problems/rotate-function/
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        sums = sum(nums)
        n = len(nums)
        
        ans = value = sum(i * val for i, val in enumerate(nums))
        for i in range(n-1, -1, -1):
            value += sums - n*nums[i]
            ans = max(ans, value)

        return ans 