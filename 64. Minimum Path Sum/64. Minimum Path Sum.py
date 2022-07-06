from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        for i, column in enumerate(grid):
            for j, num in enumerate(column):
                if i and j:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                elif i:
                    grid[i][j] += grid[i - 1][j]
                elif j:
                    grid[i][j] += grid[i][j - 1]

        return grid[-1][-1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

print(Solution().minPathSum(grid))