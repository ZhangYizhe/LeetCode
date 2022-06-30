# 54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:

![](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)

```python
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```
Example 2:

![](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)

```python
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

**Result**

```python
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
```



[Details ](https://leetcode.com/submissions/detail/734759552/)

Runtime: 45 ms, faster than 53.53% of Python3 online submissions for Spiral Matrix.

Memory Usage: 14 MB, less than 32.68% of Python3 online submissions for Spiral Matrix.

