import math

class Solution:
    def convertToBase7Naive(self, num: int) -> str:

        if num == 0: return "0"
        ans = 0
        isNegative = num < 0
        if isNegative: num *= -1
        start = math.floor(math.log(num, 7))

        while start >= 0:
            ans *= 10
            pwr = num // (7 ** start)
            if pwr > 0:
                num -= pwr * (7 ** start)
                ans += pwr
            start -= 1
            print(ans, pwr, num)
        if isNegative:
            return "-" + str(ans)
        return str(ans)

    def convertToBase7RecursiveAndSlow(self, n):
        if n < 0: return '-' + self.convertToBase7(-n)
        if n < 7:
            print("Returning n greater 7 ", n)
            return str(n);

        return self.convertToBase7(n // 7) + str(n % 7)