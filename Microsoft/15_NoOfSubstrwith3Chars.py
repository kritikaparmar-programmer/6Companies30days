# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        mydict = {'a':0, 'b':0, 'c':0}
        res = 0
        j = 0
        for i in range(0, len(s)):
            c = s[i]
            mydict[c] += 1

            while j < len(s) and mydict['a'] > 0 and mydict['b'] > 0 and mydict['c'] > 0:
                mydict[s[j]] -= 1
                j += 1
            
            res += j

        return res