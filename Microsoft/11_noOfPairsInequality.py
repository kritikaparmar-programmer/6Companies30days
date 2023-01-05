# https://leetcode.com/problems/number-of-pairs-satisfying-inequality/description/
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        count = 0
        n = len(nums1)
        diffList = []
        for i in range(n):
            diffList.append(nums1[i] - nums2[i])

        def checkcount(nums, start, mid, end, diff):
            nonlocal count
            left = start
            right = mid + 1
            while left <= mid and right <= end:
                if nums[left] <= (nums[right] + diff):
                    count += (end - right + 1)
                    left += 1
                else:
                    right += 1
            
            subarr = []
            for i in range(start, end+1):
                subarr.append(nums[i])
            subarr = sorted(subarr)
            for i in range(start, end+1):
                nums[i] = subarr[i - start]
            return 
        
        def mergeSort(nums, start, end):
            if start == end:
                return 
            mid = (start + end) // 2
            mergeSort(nums, start, mid)
            mergeSort(nums, mid + 1, end)

            checkcount(nums, start, mid, end, diff)
            return 

        mergeSort(diffList, 0, n-1)
        return count