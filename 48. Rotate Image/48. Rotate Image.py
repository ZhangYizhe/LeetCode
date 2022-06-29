from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        for layer in range(n // 2):
            first, last = layer, n - layer - 1 # 1, 2
            for i in range(first, last):
                # top
                top = matrix[layer][i]

                # left to top
                matrix[layer][i] = matrix[n - i - 1][layer] # 2, 1 -> # 1, 1

                # bottom to left
                matrix[n - i - 1][layer] = matrix[last][n - i - 1]

                # right to bottom
                matrix[last][n - i - 1] = matrix[i][last]

                # top to right
                matrix[i][last] = top




matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
Solution().rotate(matrix)
for a in matrix:
    print(a)

matrix = [[5,1,9,11],
          [2,4,8,10],
          [13,3,6,7],
          [15,14,12,16]]
Solution().rotate(matrix)
for a in matrix:
    print(a)