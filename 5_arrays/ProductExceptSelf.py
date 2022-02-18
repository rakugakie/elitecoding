#https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        for i in range(0, len(nums) - 1):
            answer[i + 1] = answer[i] * nums[i]

        multiplier = 1

        for i in reversed(range(1, len(nums))):
            multiplier = multiplier * nums[i]
            answer[i - 1] = answer[i - 1] * multiplier

        return answer