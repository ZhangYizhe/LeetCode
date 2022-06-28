# 47. Permutations II

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

```python
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
```
Example 2:

```python
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Result**

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        self.helper(nums, [], res)

        return res

    def helper(self, nums, path, res):

        if len(nums) == 1:
            return res.append(path + nums)

        tempNum = None

        for i in range(len(nums)):
            currentNum = nums[i]
            if tempNum == currentNum:
                continue
            tempNum = currentNum

            tempArr = list(nums)
            tempArr.pop(i)

            self.helper(tempArr, path + [tempNum], res)
```



[Details ](https://leetcode.com/submissions/detail/733040376/)

Runtime: 86 ms, faster than 61.47% of Python3 online submissions for Permutations II.

Memory Usage: 14.2 MB, less than 76.32% of Python3 online submissions for Permutations II.


