# 59. Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


```python
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
```
Example 2:

```python
Input: n = 1
Output: [[1]]
```

**Result**

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        num = 0
        res = []
        times = n * n
        for i in range(0, n):
            sub_res = []
            for i in range(0, n):
                sub_res.append(times)
            res.append(sub_res)

        top, bottom, left, right = 0, n - 1, 0, n - 1

        while top < bottom and left < right:

            # top
            for i in range(left, right + 1):
                num += 1
                res[top][i] = num

            top += 1

            # right
            for i in range(top, bottom + 1):
                num += 1
                res[i][right] = num

            right -= 1

            # bottom
            for i in range(right, left - 1, -1):
                num += 1
                res[bottom][i] = num

            bottom -= 1

            # left
            for i in range(bottom, top - 1, -1):
                num += 1
                res[i][left] = num

            left += 1

        return res
```



[Details ](https://leetcode.com/submissions/detail/736332849/)

Runtime: 23 ms, faster than 99.75% of Python3 online submissions for Spiral Matrix II.

Memory Usage: 13.9 MB, less than 82.26% of Python3 online submissions for Spiral Matrix II.

