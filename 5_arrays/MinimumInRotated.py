#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    def findMin(self, nums: List[int]) -> int:

        def wrapcheck(l: List[int]):
            l1 = 0;
            length = len(l)
            if length <= 3:
                return min(l)
            else:
                l1 = length // 2;

            a1 = l[0]
            a2 = l[l1 - 1]

            b1 = l[l1]
            b2 = l[length - 1]

            if a1 > a2:
                return wrapcheck(l[0:l1])
            elif b1 > b2:
                return wrapcheck(l[l1:length])
            elif a1 < b1:
                return wrapcheck(l[0:l1])
            else:
                return wrapcheck(l[l1:length])

        return wrapcheck(nums)



