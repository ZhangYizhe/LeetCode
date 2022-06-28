from typing import List

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


print(Solution().permuteUnique([-1,2,-1,2,1,-1,2,1]))