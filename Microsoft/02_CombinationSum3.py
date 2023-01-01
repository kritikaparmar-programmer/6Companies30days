# https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k, n):
        ans = []

        def combinations(ds, n, start):
            if k == len(ds):
                if n == 0:
                    ans.append(ds.copy())
                return
            for i in range(start, 10):
                ds.append(i)
                combinations(ds, n-i, i+1)
                ds.pop()
            
        combinations([], n, 1)
        return ans