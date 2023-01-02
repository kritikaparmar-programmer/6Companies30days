# https://leetcode.com/problems/bulls-and-cows/
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        hashmap1 = {}
        hashmap2 = {}

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                hashmap1[secret[i]] = 1 if secret[i] not in hashmap1 else hashmap1.get(secret[i]) + 1
                hashmap2[guess[i]] = 1 if guess[i] not in hashmap2 else hashmap2.get(guess[i]) + 1
        for key in hashmap1:
            if key in hashmap2:
                cows += min(hashmap1[key], hashmap2[key])
        ans = str(bulls) + 'A' + str(cows) + 'B'
        return ans