# 45. Jump Game II

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

 

Example 1:

```python
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
```
Example 2:

```python
Input: nums = [2,3,0,1,4]
Output: 2
```

**Result**

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        resArr = []

        self.helper(nums, 0, resArr)

        return min(resArr)


    def helper(self, nums: List[int], step: int, resArr: [int]):
        if len(nums) == 1:
            resArr.append(step)
            return

        temp_i = 1
        temp_value = 0

        for i in range(1, nums[0] + 1):

            if i >= (len(nums) - 1):
                resArr.append(step + 1)
                return

            if temp_value <= i + nums[i]:
                temp_value = nums[i] + i
                temp_i = i

        self.helper(nums[temp_i:], step + 1, resArr)
```



[Details ](https://leetcode.com/submissions/detail/733017002/)

Runtime: 454 ms, faster than 36.35% of Python3 online submissions for Jump Game II.

Memory Usage: 149.6 MB, less than 5.01% of Python3 online submissions for Jump Game II.


