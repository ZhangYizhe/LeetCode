from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:

        salary.sort()
        salary[:] = salary[1:-1]


        return sum(salary) / len(salary)

salary = [4000,3000,1000,2000]
# salary = [1000,2000,3000]

print(Solution().average(salary))