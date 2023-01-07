# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/
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