# https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        n = len(numsDivide)

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        gcdVal = numsDivide[0]
        for i in range(1, n):
            gcdVal = gcd(gcdVal, numsDivide[i])

        nums = sorted(nums)
        noOfDeletions = 0
        for i in range(0, len(nums)):
            if gcdVal % nums[i] != 0:
                noOfDeletions += 1
            else:
                break
        
        if noOfDeletions == len(nums):
            return -1
        return noOfDeletions