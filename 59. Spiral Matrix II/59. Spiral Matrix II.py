from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        num = 0
        res = []
        times = n * n
        for i in range(0, n):
            sub_res = []
            for i in range(0, n):
                sub_res.append(times)
            res.append(sub_res)

        top, bottom, left, right = 0, n - 1, 0, n - 1

        while top < bottom and left < right:

            # top
            for i in range(left, right + 1):
                num += 1
                res[top][i] = num

            top += 1

            # right
            for i in range(top, bottom + 1):
                num += 1
                res[i][right] = num

            right -= 1

            # bottom
            for i in range(right, left - 1, -1):
                num += 1
                res[bottom][i] = num

            bottom -= 1

            # left
            for i in range(bottom, top - 1, -1):
                num += 1
                res[i][left] = num

            left += 1

        return res

for arr in Solution().generateMatrix(5):
    print(arr)

