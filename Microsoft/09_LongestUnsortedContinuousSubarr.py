# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # first way - tc - o(n), sc - o(n)
        sorted_arr = sorted(nums)
        start = len(nums)
        end = 0 
        for i in range(len(nums)):
            if nums[i] != sorted_arr[i]:
                start = min(i, start)
                end = max(i, end)

        # return end - start + 1 if end - start + 1 >= 0 else 0
        # second way - tc - o(n), sc - o(1)
        mini = float('inf')
        maxi = float('-inf')
        flag = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                flag = True
            if flag is True:
                mini = min(mini, nums[i])
        flag = False
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i + 1]:
                flag = True
            if flag is True:
                maxi = max(maxi, nums[i])
        
        left, right = 0, 0
        for l in range(len(nums)):
            if mini < nums[l]:
                left = l
                break
        for r in range(len(nums)-1, -1, -1):
            if maxi > nums[r]:
                right = r
                break

        return right - left + 1 if right - left > 0 else 0   