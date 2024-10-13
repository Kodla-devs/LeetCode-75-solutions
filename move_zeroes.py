from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       
        non_zero_position = 0

        for cur in range(len(nums)):
            if nums[cur] != 0:
                nums[non_zero_position], nums[cur] = nums[cur], nums[non_zero_position]
                non_zero_position +=1 