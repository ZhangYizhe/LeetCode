# 55. Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

```python
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```
Example 2:

```python
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

**Result**

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        return self.helper(nums)

    def helper(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        temp_i = 0
        temp_max = 0

        for i in range(1, nums[0] + 1):
            if i > len(nums) - 1:
                break

            if nums[i] + i >= temp_max:
                temp_i = i
                temp_max = nums[temp_i] + i

        if temp_i > 0:
            return self.helper(nums[temp_i:])
        else:
            return False
```



[Details ](https://leetcode.com/submissions/detail/734942201/)

Runtime: 5538 ms, faster than 7.22% of Python3 online submissions for Jump Game.

Memory Usage: 412.9 MB, less than 5.16% of Python3 online submissions for Jump Game.

