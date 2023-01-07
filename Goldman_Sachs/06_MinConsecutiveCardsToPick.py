# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

# my sol
class Solution:
    def minimumCardPickup(self, cards) -> int:
        myMap = {}
        ans = []
        for i in range(len(cards)):
            if cards[i] not in myMap:
                myMap[cards[i]] = [1, i]
            else:
                ans.append(i - myMap[cards[i]][1] + 1) 
                myMap[cards[i]] = [myMap[cards[i]][0] + 1, i]

        if len(ans) == 0: return -1
        ans.sort()
        return ans[0]     


# other way
    def minimumCardPickup2(self, cards) -> int:
        lastOcc = [-1] * (int(1e7))
        ans = 1e9

        for i in range(len(cards)):
            if lastOcc[cards[i]] != -1:
                ans = min(i - lastOcc[cards[i]]  + 1, ans)
            lastOcc[cards[i]] = i

        return -1 if ans == 1e9 else ans