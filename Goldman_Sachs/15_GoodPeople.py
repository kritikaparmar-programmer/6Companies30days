# https://leetcode.com/problems/maximum-good-people-based-on-statements/description/

class Solution:
    def maximumGood(self, S):
        n, ans = len(S), 0
        def valid(cur):
            for i in range(n):
                if cur[i]:
                    for j in range(n):
                        if S[i][j] != 2 and S[i][j] != cur[j]: return False
            return True
        def dp(cur, i, cnt):
            nonlocal ans
            if i == n:
                if valid(cur): ans = max(ans, cnt)
                return
            cur.append(0)
            dp(cur, i+1, cnt)
            cur[-1] = 1
            dp(cur, i+1, cnt+1)
            cur.pop()
        
        dp([], 0, 0)
        return ans