from typing import List


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


print(Solution().permute([1,2,3]))
print(Solution().permute([0,1]))
print(Solution().permute([1]))