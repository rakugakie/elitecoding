#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer_heap = {}

        for i in range(0, len(nums)):
            if answer_heap.get(nums[i]) is None:
                answer_heap[target - nums[i]] = i
            else:
                return [i, answer_heap.get(nums[i])]