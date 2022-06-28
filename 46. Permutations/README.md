# 46. Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

```python
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```
Example 2:

```python
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```
Example 3:

```python
Input: nums = [1]
Output: [[1]]
```

**Result**

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        self.helper(nums, [], res)

        return res


    def helper(self, nums: List[int], path: List[int], res: List[List[int]]):

        if len(nums) == 0:
            res.append(path)

        for i in range(len(nums)):
            tempList = list(nums)
            tempList.pop(i)

            self.helper(tempList, path + [nums[i]], res)
```



[Details ](https://leetcode.com/submissions/detail/733024335/)

Runtime: 54 ms, faster than 63.79% of Python3 online submissions for Permutations.

Memory Usage: 13.9 MB, less than 83.79% of Python3 online submissions for Permutations.

