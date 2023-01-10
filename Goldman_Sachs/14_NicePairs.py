# https://leetcode.com/problems/count-nice-pairs-in-an-array
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            reversed_num = 0
            while num != 0:
                digit = num % 10
                reversed_num = reversed_num * 10 + digit
                num //= 10
            return reversed_num

        mp = {}
        ans = 0
        for i in range(len(nums)):
            val = nums[i] - rev(nums[i])
            ans += 0 if val not in mp else mp[val]
            mp[val] = 1 if val not in mp else mp[val] + 1

        return ans % int(1e9 + 7)