from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return self.helper([], digits)

    def helper(self, pre_strs, rest_digits):
        if len(rest_digits) == 0:
            return pre_strs

        temp_strs = []

        for s in self.putLetters(int(rest_digits[0])):

            if len(pre_strs) == 0:
                temp_strs.append(s)
                continue

            for c in pre_strs:
                temp_strs.append(c + s)


        return self.helper(temp_strs, rest_digits[1:len(rest_digits)])

    def putLetters(self, num: int) -> str:
        if num == 2:
            return "abc"
        elif num == 3:
            return "def"
        elif num == 4:
            return "ghi"
        elif num == 5:
            return "jkl"
        elif num == 6:
            return "mno"
        elif num == 7:
            return "pqrs"
        elif num == 8:
            return "tuv"
        elif num == 9:
            return "wxyz"
        else:
            return ""

print(Solution().letterCombinations("23"))