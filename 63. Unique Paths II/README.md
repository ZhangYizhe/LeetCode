# 63. Unique Paths II

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:

![](https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg)

```python
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```
Example 2:

![](https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg)

```python
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
```

**Result**

```python
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
```



[Details ](https://leetcode.com/submissions/detail/737957697/)

Runtime: 72 ms, faster than 33.03% of Python3 online submissions for Unique Paths II.

Memory Usage: 13.9 MB, less than 74.15% of Python3 online submissions for Unique Paths II.

