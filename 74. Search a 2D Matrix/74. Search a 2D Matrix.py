from typing import List
import copy

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for x in range(0, len(matrix)):
            if target < matrix[x][0]:
                break

            if target > matrix[x][-1]:
                continue

            left = 0
            right = len(matrix[x]) - 1

            while (left <= right):
                if matrix[x][left] == target or matrix[x][right] == target:
                    return True

                left += 1
                right -= 1


        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 13

# matrix = [[1]]
# target = 1

print(Solution().searchMatrix(matrix, target))