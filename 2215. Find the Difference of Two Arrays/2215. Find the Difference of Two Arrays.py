from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        nums1[:] = list(set(nums1))
        nums2[:] = list(set(nums2))

        nums1.sort()
        nums2.sort()

        nums1Index = 0
        nums2Index = 0

        result = [[], []]

        while (nums1Index < len(nums1) and nums2Index < len(nums2)):

                num1 = nums1[nums1Index]
                num2 = nums2[nums2Index]

                if num1 == num2:
                    nums1Index += 1
                    nums2Index += 1

                elif num1 > num2:
                    result[1] += [num2]
                    nums2Index += 1
                elif num1 < num2:
                    result[0] += [num1]
                    nums1Index += 1

        result[0] += nums1[nums1Index:]
        result[1] += nums2[nums2Index:]


        return result

nums1 = [1,2,3]
nums2 = [2,4,6]

nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]

# nums1 = [26,48,-78,-25,42,-8,94,-68,26]
# nums2 = [61,-17]

# nums1 = [52,-21]
# nums2 = [22,66,89,52,-56,5,22,-70,99]

print(Solution().findDifference(nums1, nums2))