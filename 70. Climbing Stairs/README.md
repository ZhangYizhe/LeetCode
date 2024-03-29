# 70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

```python
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```
Example 2:

```python
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

**Result**

```python
class Solution:
    def climbStairs(self, n: int) -> int:

        sums = {}

        res = self.helper(n, sums)

        return res

    def helper(self, n, sums):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif n in sums:
            return sums[n]
        else:
            value = self.helper(n - 1, sums) + self.helper(n - 2, sums)
            sums[n] = value
            return value
```



[Details ](https://leetcode.com/submissions/detail/739711386/)

Runtime: 51 ms, faster than 33.22% of Python3 online submissions for Climbing Stairs.

Memory Usage: 13.9 MB, less than 57.08% of Python3 online submissions for Climbing Stairs.

