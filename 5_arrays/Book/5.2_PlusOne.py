class Solution:
    def naivePlusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits) - 1] += 1
        if len(digits) == 1:
            if digits[0] == 10:
                return [1, 0]
            else:
                return digits

        for i in reversed(range(0, len(digits))):

            if digits[i] >= 10:
                if i > 0:
                    digits[i] = 0
                    digits[i - 1] += 1
                else:
                    digits[i] = 1
                    digits.append(0)
            else:
                return digits
        return digits

    def bookPlusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1

        for i in reversed(range(0, len(digits))):

            if digits[i] == 10:
                if i > 0:
                    digits[i] = 0
                    digits[i - 1] += 1
            else:
                break

        if digits[0] == 10:
            digits[0] = 1
            digits.append(0)
        return digits