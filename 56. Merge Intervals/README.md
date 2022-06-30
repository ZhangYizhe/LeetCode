# 56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

```python
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
```
Example 2:

```python
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

**Result**

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        res = []

        l, r = intervals[0]

        for i in range(1, len(intervals)):
            c_l, c_r = intervals[i]

            if r >= c_l:
                if c_r > r:
                    r = c_r
            else:
                res.append([l, r])
                l, r = c_l, c_r

        res.append([l, r])

        return res
```



[Details ](https://leetcode.com/submissions/detail/734961230/)

Runtime: 153 ms, faster than 92.46% of Python3 online submissions for Merge Intervals.

Memory Usage: 18.8 MB, less than 25.35% of Python3 online submissions for Merge Intervals.

