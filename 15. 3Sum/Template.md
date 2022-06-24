# 15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

```python
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```
Example 2:

```python
Input: nums = []
Output: []
```
Example 3:

```python
Input: nums = [0]
Output: []
```

**Result**

```Python3
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []

        for index_first in range(len(nums)):

            if index_first > 0 and nums[index_first] == nums[index_first - 1]:
                continue

            index_sec = index_first + 1
            index_third = len(nums) - 1
            while (index_sec < index_third):

                if index_third < len(nums) - 1 and nums[index_third] == nums[index_third + 1]:
                    index_third -= 1
                    continue

                sum_num = nums[index_first] + nums[index_sec] + nums[index_third]

                if sum_num < 0:
                    index_sec += 1
                else:
                    if sum_num == 0:
                        result.append([nums[index_first], nums[index_sec], nums[index_third]])
                    index_third -= 1

        return result
```



[Details ](https://leetcode.com/submissions/detail/729747370/)

Runtime: 1334 ms, faster than 47.80% of Python3 online submissions for 3Sum.

Memory Usage: 18.1 MB, less than 41.54% of Python3 online submissions for 3Sum.

