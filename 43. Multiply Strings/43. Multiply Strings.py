class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        res = ""

        num1 = num1[::-1]
        num2 = num2[::-1]

        if len(num1) < len(num2):
            temp = num2
            num2 = num1
            num1 = temp

        step_arr = []

        for num in num2:
            step_arr.append(self.helper(num1, int(num)))

        high = 0

        for i in range((len(step_arr) - 1)  + len(step_arr[-1])):

            sum = 0

            for j in range(len(step_arr)):
                if j > i:
                    break
                _i = i - j

                if _i > len(step_arr[j]) - 1:
                    continue

                sum += int(step_arr[j][_i])

            str_sum = str(sum + high)

            if len(str_sum) > 1:
                high = int(str_sum[:-1])
            else:
                high = 0

            res += str_sum[-1]

        if high > 0:
            res += str(high)

        res = res[::-1]

        while res[0] == "0" and len(res) > 1:
            res = res[1:]

        return res


    def helper(self, top: str, bottom: int) -> str:

        res = ""
        high = 0

        for num in top:
            num_str = str(int(num) * bottom + high)
            res += num_str[-1]
            if len(num_str) > 1:
                high = int(num_str[:-1])
            else:
                high = 0

        if high > 0:
            res += str(high)

        return res


print(Solution().multiply("0", "456"))