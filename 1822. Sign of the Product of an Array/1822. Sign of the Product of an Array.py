from typing import List
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        nums.sort()

        negativeCount = 0

        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                negativeCount += 1

        if negativeCount % 2 == 0:
            return 1
        else:
            return -1


        return 0

nums = [-1,-2,-3,-4,3,2,1]
# nums = [1,5,0,2,-3]
# nums = [-1,1,-1,1,-1]

print(Solution().arraySign(nums))