from typing import List

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#
#         return self.helper(nums)
#
#     def helper(self, nums: List[int]) -> bool:
#         if len(nums) == 1:
#             return True
#
#         temp_i = 0
#         temp_max = 0
#
#         for i in range(1, nums[0] + 1):
#             if i > len(nums) - 1:
#                 break
#
#             if nums[i] + i >= temp_max:
#                 temp_i = i
#                 temp_max = nums[temp_i] + i
#
#         if temp_i > 0:
#             return self.helper(nums[temp_i:])
#         else:
#             return False

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + n)

        return True


print(Solution().canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]))

print(Solution().canJump([2,3,1,1,4])) # True

print(Solution().canJump([3,2,1,0,4])) # False

print(Solution().canJump([5,9,3,2,1,0,2,3,3,1,0,0])) # True