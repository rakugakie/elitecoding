#https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = None
        current_sum = None
        for num in nums:

            if max_sum is None or num > 0 and max_sum <= 0:
                max_sum = num
                current_sum = num
            else:

                current_sum = current_sum + num
                if current_sum > max_sum:
                    max_sum = current_sum
                elif current_sum < 0:
                    if num > max_sum:
                        max_sum = num
                    else:
                        current_sum = min(0, max_sum)
        return max_sum