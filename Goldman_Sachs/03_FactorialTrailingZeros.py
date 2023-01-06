# https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        power = 5
        while (n // power > 0):
            ans += n // power
            power *= 5
        return ans