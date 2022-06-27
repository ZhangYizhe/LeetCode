from typing import List

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


print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))