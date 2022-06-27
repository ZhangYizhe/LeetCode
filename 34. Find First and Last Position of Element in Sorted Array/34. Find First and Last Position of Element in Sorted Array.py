from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return [-1, -1]

        l, r = 0, len(nums) - 1
        mid = (l + r) // 2

        while nums[l] != nums[r]:
            if target == nums[mid]:
                if nums[l] < target:
                    l = l + 1
                if nums[r] > target:
                    r = r - 1
            elif target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1

            mid = (l + r) // 2

        if nums[l] != target:
            return [-1, -1]


        return [l, r]



print(Solution().searchRange([10, 10, 11], 10))