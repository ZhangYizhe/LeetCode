from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []

        for index_first in range(len(nums)):

            if index_first > 0 and nums[index_first] == nums[index_first - 1]:
                continue

            index_sec = index_first + 1
            index_third = len(nums) - 1
            while (index_sec < index_third):

                if index_third < len(nums) - 1 and nums[index_third] == nums[index_third + 1]:
                    index_third -= 1
                    continue

                sum_num = nums[index_first] + nums[index_sec] + nums[index_third]

                if sum_num < 0:
                    index_sec += 1
                else:
                    if sum_num == 0:
                        result.append([nums[index_first], nums[index_sec], nums[index_third]])
                    index_third -= 1

        return result



print(Solution().threeSum([1,-1,-1,0]))