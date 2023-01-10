# https://leetcode.com/problems/invalid-transactions/description/
import collections
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        hashmap = collections.defaultdict(list)
        invalid = set()
        for i, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(',')
            
            if int(amount) > 1000:
                invalid.add(i)
            
            if name in hashmap:
                for prev_trans, idx in hashmap[name]:
                    _, prev_time, _, prev_city = prev_trans.split(',')
                    if abs(int(time) - int(prev_time)) <= 60 and prev_city != city:
                        invalid.add(idx)
                        invalid.add(i)
                        
            hashmap[name].append((transaction, i))
        
        ans = []
        for i in invalid:
            ans.append(transactions[i])
        return ans