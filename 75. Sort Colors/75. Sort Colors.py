from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        numsDict = [0] * 3

        for num in nums:
            numsDict[num] += 1

        nums[:] = [0] * numsDict[0] + [1] * numsDict[1] + [2] * numsDict[2]

nums = [2,0,2,1,1,0]
nums = [2,0,1]
nums = [2]

Solution().sortColors(nums)
print(nums)