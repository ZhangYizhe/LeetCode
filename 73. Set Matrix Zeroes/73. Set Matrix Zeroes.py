from typing import List
import copy

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        tempMatrix = copy.deepcopy(matrix)

        for x in range(0, len(matrix)):
            for y in range(0, len(matrix[x])):
                num = matrix[x][y]
                if num == 0:
                    tempMatrix[x][:] = [0] * len(tempMatrix[x])

                    for _x in range(0, len(matrix)):
                        tempMatrix[_x][y] = 0

        matrix[:] = tempMatrix[:]





def printMatrix(matrix):
    for arr in matrix:
        print(arr)

    print("======")

    Solution().setZeroes(matrix)

    for arr in matrix:
        print(arr)

matrix = [[1,1,1],[1,0,1],[1,1,1]]
# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

printMatrix(matrix)


