from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        res = []

        l, r = intervals[0]

        for i in range(1, len(intervals)):
            c_l, c_r = intervals[i]

            if r >= c_l:
                if c_r > r:
                    r = c_r
            else:
                res.append([l, r])
                l, r = c_l, c_r

        res.append([l, r])

        return res


print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))

print(Solution().merge([[1,4],[4,5]]))

print(Solution().merge([[1,4],[0,4]]))

print(Solution().merge([[1,4],[2,3]]))
