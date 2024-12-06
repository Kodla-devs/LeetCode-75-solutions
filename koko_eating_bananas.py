from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k):
            total_hours = 0
            for pile in piles:
                total_hours += (pile + k - 1) // k
            return total_hours <= h
        
        left, right = 1, max(piles)
        result = right
        while left <= right:
            mid = (left + right) // 2
            if canFinish(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result