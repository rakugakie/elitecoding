#https://leetcode.com/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        for i in range(32):
            ones = ones + (n & 1)
            n = n >> 1
        return ones