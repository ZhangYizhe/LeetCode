from typing import List
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        fromArr = set({})
        toArr = set({})

        for item in edges:
            fromArr.add(item[0])
            toArr.add(item[1])

        return fromArr - toArr


n = 6
edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]

print(Solution().findSmallestSetOfVertices(n, edges))