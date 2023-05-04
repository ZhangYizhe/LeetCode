import copy
from typing import List

class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        senate = list(senate)

        length = len(senate)

        r_arr = []
        d_arr = []

        for i in range(len(senate)):
            if senate[i] == "R":
                r_arr += [i]
            else:
                d_arr += [i]

        while r_arr and d_arr:
            r_senate = r_arr.pop(0)
            d_senate = d_arr.pop(0)

            if r_senate < d_senate:
                r_arr += [r_senate + length]
            else:
                d_arr += [d_senate + length]

        if len(r_arr) == 0:
            return "Dire"
        else:
            return "Radiant"

        # hasDiff = True
        #
        # while len(senateArr) > 1 and hasDiff:
        #
        #     index = 0
        #     nextIndex = index + 1
        #     while index < len(senateArr) and hasDiff:
        #         hasDiff = False
        #
        #         for _nextIndex in (list(range(nextIndex, len(senateArr))) + list(range(0, index))):
        #             if senateArr[index] != senateArr[_nextIndex]:
        #                 hasDiff = True
        #                 senateArr.pop(_nextIndex)
        #                 nextIndex = _nextIndex
        #                 break
        #             else:
        #                 continue
        #
        #         index = index + 1
        #
        # if senateArr[0] == "R":
        #     return "Radiant"
        # else:
        #     return "Dire"

senate = "RRRRRDDRDRDRDDDRDDDRRRDDDRDDR"
import time
start_time = time.time()

print(Solution().predictPartyVictory(senate))

print("--- %s seconds ---" % (time.time() - start_time))
