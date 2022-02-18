class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        is_positive = True
        if len(s) <= 0:
            return 0

        if s[0] == '-':
            is_positive = False
            s = s[1:]

        elif s[0] == '+':
            s = s[1:]

        for c in range(len(s)):
            if (ord(s[c]) < 48) or ord(s[c]) > 57:
                s = s[:c]
                break;

        ret_int = 0
        for c in range(len(s)):
            integer = ord(s[len(s) - 1 - c]) % 48
            ret_int += integer * (10 ** c)
            # print("index: ", s[len(s) - 1 - c], integer, max(1, (c * 10)), ret_int)

        if not is_positive:
            ret_int *= -1

        if ret_int > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif ret_int < -2 ** 31:
            return -2 ** 31

        return ret_int