import bisect
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        result = []

        for spell in spells:
            index = bisect.bisect_left(potions, success / spell)
            result.append(len(potions) - index)
        
        return result
