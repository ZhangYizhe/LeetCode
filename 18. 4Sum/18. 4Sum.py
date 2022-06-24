from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()

        res = []

        for index_1 in range(len(nums)):
            if index_1 > 0 and nums[index_1] == nums[index_1 - 1]:
                continue

            for index_2 in range(index_1 + 1, len(nums)):

                if index_2 > index_1 + 1 and nums[index_2] == nums[index_2 - 1]:
                    continue

                l = index_2 + 1
                r = len(nums) - 1

                while l < r:

                    if r < len(nums) - 1 and nums[r] == nums[r + 1]:
                        r -= 1
                        continue

                    sum = nums[index_1] + nums[index_2] + nums[l] + nums[r]

                    if sum < target:
                        l += 1
                    else:
                        if sum == target:
                            res.append([nums[index_1], nums[index_2], nums[l], nums[r]])
                        r -= 1

        return res


print(Solution().fourSum([-2,-1,-1,1,1,2,2], 0))