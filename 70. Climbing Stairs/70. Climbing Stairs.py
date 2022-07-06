class Solution:
    def climbStairs(self, n: int) -> int:

        sums = {}

        res = self.helper(n, sums)

        return res

    def helper(self, n, sums):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif n in sums:
            return sums[n]
        else:
            value = self.helper(n - 1, sums) + self.helper(n - 2, sums)
            sums[n] = value
            return value

print(Solution().climbStairs(46)) #3
