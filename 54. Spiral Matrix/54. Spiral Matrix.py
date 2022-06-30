from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []

        top, right, bottom, left = 0, len(matrix[0]), len(matrix), 0

        while top < bottom and left < right:

            for i in range(left, right):
                res.append(matrix[top][i])

            top += 1

            if left < right:
                for i in range(top, bottom):
                    res.append(matrix[i][right - 1])

            right -= 1

            if top < bottom:
                for i in range(right - 1, left, -1):
                    res.append(matrix[bottom - 1][i])

            bottom -= 1

            if left < right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])

            left += 1

        return res

print(Solution().spiralOrder([[6,9,7]]))
# [6,9,7]

print(Solution().spiralOrder([[1],[4]]))
# [1, 4]

print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
# [1,2,3,6,9,8,7,4,5]

print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
# [1,2,3,4,8,12,11,10,9,5,6,7]