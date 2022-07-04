from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)

        arr = [1] * n

        arr[0] = 1 - obstacleGrid[0][0]

        for i in range(1, n):
            arr[i] = arr[i - 1] * (1 - obstacleGrid[i][0])

        for j in range(1, m):
            arr[0] *= (1 - obstacleGrid[0][j])
            for i in range(1, n):
                arr[i] = (arr[i - 1] + arr[i]) * (1 - obstacleGrid[i][j])

        return arr[-1]


print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))

print(Solution().uniquePathsWithObstacles([[0,1],[0,0]]))

print(Solution().uniquePathsWithObstacles([[1,0],[0,0]]))

print(Solution().uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))

print(Solution().uniquePathsWithObstacles([[0],[1]]))