# 50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

```python
Input: x = 2.00000, n = 10
Output: 1024.00000
```
Example 2:

````python
Input: x = 2.10000, n = 3
Output: 9.26100
````
Example 3:

```python
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
```

**Result**

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2:
            return x * self.myPow(x, n - 1)

        return self.myPow(x * x, n//2)
```



[Details ](https://leetcode.com/submissions/detail/734194235/)

Runtime: 64 ms, faster than 11.64% of Python3 online submissions for Pow(x, n).

Memory Usage: 13.9 MB, less than 67.81% of Python3 online submissions for Pow(x, n).

