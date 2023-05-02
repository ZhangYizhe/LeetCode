from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def recursion(start: int, end: int, rest: int) -> []:
            if rest < 0:
                return None

            allItems = []

            for num in range(start, end):
                subItems = recursion(num + 1, end, rest - 1)
                if subItems == None:
                    allItems += [[num]]
                else:
                    for subNum in subItems:
                            allItems += [[num] + subNum]
            return allItems


        return recursion(1, n + 1, k - 1)

n = 4
k = 4
print(Solution().combine(n, k))