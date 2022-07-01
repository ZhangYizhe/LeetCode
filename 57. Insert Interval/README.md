# 57. Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

```python
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```
Example 2:

```python
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

**Result**

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        if len(intervals) == 0:
            return [newInterval]
        elif len(newInterval) == 0:
            return intervals

        l, r = intervals[0]

        n_l, n_r = newInterval

        if len(intervals) == 1:
            if n_r < l:
                res.append([n_l, n_r])
                n_r = -1
            elif n_l <= r:
                if n_l < l:
                    l = n_l
                if n_r > r:
                    r = n_r
                n_r = -1
        else:
            for i in range(1, len(intervals)):
                c_l, c_r = intervals[i]

                if n_r > 0:
                    if n_r < l:
                        res.append([n_l, n_r])
                        n_r = -1
                    elif n_l <= r:
                        if n_l < l:
                            l = n_l
                        if n_r > r:
                            r = n_r
                        n_r = -1

                if r < c_l:
                    res.append([l, r])
                    l, r = c_l, c_r

                else:
                    if c_r > r:
                        r = c_r

        if n_r > 0:
            if n_r < l:
                res.append([n_l, n_r])
            elif n_l <= r:
                if n_l < l:
                    l = n_l
                if n_r > r:
                    r = n_r
            else:
                res.append([l, r])
                l, r = n_l, n_r

        res.append([l, r])

        return res
```



[Details ](https://leetcode.com/submissions/detail/735776424/)

Runtime: 87 ms, faster than 89.26% of Python3 online submissions for Insert Interval.

Memory Usage: 17.3 MB, less than 53.65% of Python3 online submissions for Insert Interval.

