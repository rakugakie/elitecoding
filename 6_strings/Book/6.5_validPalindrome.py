class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).upper()

        for i in range(len(s) // 2):

            if s[i] != s[-i - 1]:
                return False
        return True

    def isPalindromePointers(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            if not s[start].isalnum():
                start += 1

            elif not s[end].isalnum():
                end -= 1
            else:

                if s[start].lower() != s[end].lower():
                    return False
                start += 1
                end -= 1

        return True
