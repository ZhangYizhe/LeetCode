# 64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:

![](https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg)


```python
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
```
Example 2:

```python
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
```

**Result**

```python
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
```



[Details ](https://leetcode.com/submissions/detail/739697366/)

Runtime: 210 ms, faster than 15.45% of Python3 online submissions for Minimum Path Sum.

Memory Usage: 15.6 MB, less than 83.85% of Python3 online submissions for Minimum Path Sum.

