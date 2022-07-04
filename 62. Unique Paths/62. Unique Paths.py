# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#
#         resArr = []
#
#         self.helper(m - 1, n - 1, resArr)
#
#         return len(resArr)
#
#     def helper(self, m, n, resArr):
#         if m == 0 and n == 0:
#             resArr.append(1)
#
#         if m > 0:
#             self.helper(m - 1, n, resArr)
#
#         if n > 0:
#             self.helper(m, n - 1, resArr)
from itertools import product

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [1] * n
        for _, j in product(range(1, m), range(1, n)):
            arr[j] += arr[j - 1]

        return arr[-1]


print(Solution().uniquePaths(4, 5))
print(Solution().uniquePaths(3, 6))
# print(Solution().uniquePaths(20, 10))