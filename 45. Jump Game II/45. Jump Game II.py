from typing import List

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


print(Solution().jump([2,3,1,1,4]))
print(Solution().jump([2,3,1]))
print(Solution().jump([1,3,2]))
print(Solution().jump([1]))
print(Solution().jump([5,6,4,4,6,9 ,4,4,7,4,4,8,2,6,8 ,1,5,9,6,5,2,7,9 ,7,9,6,9,4,1,6,8,8 ,4,4,2,0,3,8,5]))