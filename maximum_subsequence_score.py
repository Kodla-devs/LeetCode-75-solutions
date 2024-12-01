from heapq import heappop, heappush
from operator import itemgetter
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res, prefixSum, minHeap = 0, 0, []
        combined = sorted(list(zip(nums1, nums2)), key=itemgetter(1), reverse=True)

        for a, b in combined:
            prefixSum += a
            heappush(minHeap, a)
            if len(minHeap) == k:
                res = max(res, prefixSum * b)
                prefixSum -= heappop(minHeap)

        return res 
