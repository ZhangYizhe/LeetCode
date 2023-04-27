from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 1:
            return

        maxNum = None
        for i in range(0, len(nums) - 1):
            if nums[i + 1] > nums[i]:
                maxNum = nums[i]


        maxNumIndex = len(nums) - 1

        for x in range(len(nums) - 2, -1, -1):

            lnum = nums[x]
            rnum = nums[x + 1]

            if lnum < rnum:
                maxNum = nums[maxNumIndex]

                if maxNum > lnum and maxNum < rnum:
                    tempNums = [lnum] + nums[x + 1:maxNumIndex] + nums[maxNumIndex + 1:]
                    tempNums.sort()
                    nums[:] = nums[:x] + [maxNum] + tempNums
                    return

                tempNum = [lnum] + nums[x + 1 + 1:]
                tempNum.sort()
                nums[:] = nums[:x] + [rnum] + tempNum

                return

            if maxNum != None and nums[maxNumIndex] - maxNum <= 0:
                maxNumIndex = x + 1

        nums.sort()

# nums = [1, 2, 3]
nums = [1, 3, 2]
# nums = [2, 1, 3]
# nums = [2, 3, 1]
# nums = [3, 2, 1]
# nums = [1, 2, 3]
# nums = [1]
# nums = [5,4,7,5,3,2]
nums = [1, 5, 1]
# nums = [2,2,7,5,4,3,2,2,1]

Solution().nextPermutation(nums)

print("nums = " + str(nums))
