from collections import defaultdict
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        operations = 0
        
        for num in nums:
            complement = k - num
            if counts[complement] > 0:
                operations += 1
                counts[complement] -= 1
            else:
                counts[num] += 1
        
        return operations