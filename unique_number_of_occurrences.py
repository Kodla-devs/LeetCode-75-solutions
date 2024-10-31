from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        dic = {}

        for num in arr:
            dic[num] = dic.get(num, 0) + 1

        occurrences = dic.values()

        return len(occurrences) == len(set(occurrences))