from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = [0]

        for i in range(1, n+1):
            counter.append(counter[i>>1] + (i & 1))
        
        return counter