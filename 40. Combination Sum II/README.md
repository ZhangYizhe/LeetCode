# 40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

```python
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
```
Example 2:

```python
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
```

**Result**

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.helper(candidates, target, [], res)

        return res

    def helper(self, candidates: List[int], target, path: List[int], res: List[List[int]]):

        if target < 0:
            return

        if target == 0:
            return res.append(path)

        for i in range(len(candidates)):

            if i > 0 and candidates[i] == candidates[i - 1]:
                continue

            temp_candidates = list(candidates)
            temp_candidates.pop(i)

            self.helper(temp_candidates[i:], target - candidates[i], path + [candidates[i]], res)
```



[Details ](https://leetcode.com/submissions/detail/732389010/)

Runtime: 194 ms, faster than 12.57% of Python3 online submissions for Combination Sum II.

Memory Usage: 14 MB, less than 57.89% of Python3 online submissions for Combination Sum II.

