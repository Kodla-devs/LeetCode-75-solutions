from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda interval: interval[1])
        non_overlapping_end = float('-inf')
        removal_count = 0

        for start, end in intervals:
            if start >= non_overlapping_end:
                non_overlapping_end = end
            else:
                removal_count += 1
        
        return removal_count
        