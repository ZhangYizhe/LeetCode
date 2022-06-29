# 53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

```python
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```
Example 2:

```python
Input: nums = [1]
Output: 1
```
Example 3:

```python
Input: nums = [5,4,-1,7,8]
Output: 23
```

**Result**

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max, till_now_max = 0, float('-inf')

        for num in nums:
            cur_max = max(num, cur_max + num)
            till_now_max = max(cur_max, till_now_max)

        return till_now_max
```



[Details ](https://leetcode.com/submissions/detail/734232959/)

Runtime: 830 ms, faster than 79.67% of Python3 online submissions for Maximum Subarray.

Memory Usage: 27.9 MB, less than 77.69% of Python3 online submissions for Maximum Subarray.

