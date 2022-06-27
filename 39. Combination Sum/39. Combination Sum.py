from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.helper(candidates, target, [], res)
        return res

    def helper(self, candidates: List[int], target: int, path: List[int], res: List[List[int]]):
        if target < 0:
            return

        if target == 0:
            return res.append(path)

        for i in range(len(candidates)):
            self.helper(candidates[i:], target - candidates[i], path + [candidates[i]], res)

print(Solution().combinationSum([2,3,6,7], 7))