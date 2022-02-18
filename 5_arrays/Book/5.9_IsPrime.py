class Solution:
    def countPrimes(self, n: int) -> int:

        if n <= 2:
            return 0

        is_prime = [False] + [True] * (n)
        count = 0

        for i in range(0, n - 1):
            if is_prime[i]:
                for p in range(i + i + 1, n, (i + 1)):
                    is_prime[p] = False

                count += 1

        return count