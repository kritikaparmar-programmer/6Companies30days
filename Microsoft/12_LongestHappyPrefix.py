# https://leetcode.com/problems/longest-happy-prefix/
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0] * n
        j = 0
        for i in range(1, n):
            while s[i] != s[j] and j > 0:
                j = lps[j - 1] # we will keep resetting until found match 

            if s[i] == s[j]: # if j moved back to 0
                lps[i] = j + 1
                j += 1
        print(lps)
        return s[:lps[-1]]