from typing import List

class Solution:
    # def average(self, salary: List[int]) -> float:
    #
    #     salary.sort()
    #     salary[:] = salary[1:-1]
    #
    #
    #     return sum(salary) / len(salary)

    def average(self, salary: List[int]) -> float:
        salary.sort()
        return sum(salary[1:-1]) / (len(salary) - 2)



salary = [4000,3000,1000,2000]
# salary = [1000,2000,3000]

print(Solution().average(salary))