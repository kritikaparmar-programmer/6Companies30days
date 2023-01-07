# https://leetcode.com/problems/split-array-into-consecutive-subsequences/

class Solution:
    def isPossible(self, nums) -> bool:
        availableMap = {}
        vacancyMap = {}
        for i in nums:
            availableMap[i] = 1 if i not in availableMap else availableMap[i] + 1

        for num in nums:
            # if num not available lets abort
            if num not in availableMap or availableMap[num] == 0:
                continue
            
            # if num available check if someone else is looking for that num  
            elif num in vacancyMap and vacancyMap[num] > 0:
                availableMap[num] -= 1
                vacancyMap[num] -= 1
                vacancyMap[num + 1] = 1 if num + 1 not in vacancyMap else vacancyMap[num + 1] + 1
            
            elif num in availableMap and num + 1 in availableMap and num + 2 in availableMap and availableMap[num] > 0 and availableMap[num + 1] > 0 and availableMap[num + 2] > 0:
                availableMap[num] -= 1
                availableMap[num + 1] -= 1
                availableMap[num + 2] -= 1
                vacancyMap[num + 3] = 1 if num + 3 not in vacancyMap else vacancyMap[num + 3] + 1

            else:
                return False
        
        return True