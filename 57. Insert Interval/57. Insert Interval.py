from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        if len(intervals) == 0:
            return [newInterval]
        elif len(newInterval) == 0:
            return intervals

        l, r = intervals[0]

        n_l, n_r = newInterval

        if len(intervals) == 1:
            if n_r < l:
                res.append([n_l, n_r])
                n_r = -1
            elif n_l <= r:
                if n_l < l:
                    l = n_l
                if n_r > r:
                    r = n_r
                n_r = -1
        else:
            for i in range(1, len(intervals)):
                c_l, c_r = intervals[i]

                if n_r > 0:
                    if n_r < l:
                        res.append([n_l, n_r])
                        n_r = -1
                    elif n_l <= r:
                        if n_l < l:
                            l = n_l
                        if n_r > r:
                            r = n_r
                        n_r = -1

                if r < c_l:
                    res.append([l, r])
                    l, r = c_l, c_r

                else:
                    if c_r > r:
                        r = c_r

        if n_r > 0:
            if n_r < l:
                res.append([n_l, n_r])
            elif n_l <= r:
                if n_l < l:
                    l = n_l
                if n_r > r:
                    r = n_r
            else:
                res.append([l, r])
                l, r = n_l, n_r

        res.append([l, r])

        return res


print(Solution().insert([[1,5]], [5,7]))
# [[1,5],[6,9]]

print(Solution().insert([[6,7],[8,10],[12,16]], [16, 20]))
# [[1,2],[3,10],[12,16]]