from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        self.helper(n, n, "", res)

        return res

    def helper(self, left: int, right: int, s: str, res: List[str]):
        if left == 0 and right == 0:
            res.append(s)
            return

        if left != 0:
            self.helper(left-1, right, s + "(", res)

        if left < right:
            self.helper(left, right-1, s + ")", res)

print(Solution().generateParenthesis(3))