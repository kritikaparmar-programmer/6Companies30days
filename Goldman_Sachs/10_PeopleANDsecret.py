# https://leetcode.com/problems/number-of-people-aware-of-a-secret/description/
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * (n + 1)  # dp[0] = 0
        dp[1] = 1
        
        for i in range(1, n+1):
            if dp[i] > 0:
                lower = i + delay # for i = 1, lower = 3
                upper = i + forget # for i = 1, upper = 5
                upper_bound = min(upper, n+1) # upper_bound = 5
                for j in range(lower, upper_bound):
                    dp[j] += dp[i]

                if upper <= n: # the person will forget after upper
                    dp[i] = 0
        
        return sum(dp) % int((1e9 + 7))