class Solution:
    def longestSubarray(self, nums):
        l=r=0
        max_ones = 0
        dele_pos = -1

        for r in range(len(nums)):
            if nums[r] == 0:
                max_ones = max(max_ones, r - l - 1)
                l = dele_pos + 1
                dele_pos = r
            elif r == len(nums) - 1:
                max_ones = max(max_ones, r - l)
        
        return max_ones