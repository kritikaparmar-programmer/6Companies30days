# https://leetcode.com/problems/ipo
from heapq import *
class Solution:
    def findMaximizedCapital(self, max_projects: int, initial_capital: int, profits: List[int], capital: List[int]) -> int:
        capital_heap = []
        profits_heap = []

		# insert all project capitals to a min-heap
        for i in range(len(capital)):
            heappush(capital_heap, (capital[i], i))
        
		# let's try to find a total of 'numberOfProjects' best projects
        available_capital = initial_capital
        for i in range(max_projects):
			# find all projects that can be selected within the available capital and insert them in a max-heap
            while capital_heap and capital_heap[0][0] <= available_capital:
                curr_cap, i = heappop(capital_heap)
                heappush(profits_heap, (-profits[i], i))
            
			# terminate if we are not able to find any project that can be completed within the available capital
            if not profits_heap:
                break
            
			# select the project with the maximum profit
            available_capital += -heappop(profits_heap)[0]
        return available_capital