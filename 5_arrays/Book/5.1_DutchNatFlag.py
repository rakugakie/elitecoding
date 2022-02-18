class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i_0 = 0
        i_2 = len(nums) - 1
        i = 0
        pivot = 1
        while (i <= i_2):
            if nums[i] > pivot:
                nums[i], nums[i_2] = nums[i_2], nums[i]
                i_2 -= 1
            elif nums[i] == pivot:
                i += 1
            else:
                nums[i], nums[i_0] = nums[i_0], nums[i]
                i_0 += 1
                i += 1
        return nums

