from typing import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if set(word1) != set(word2):
            return False
        
        freq1 = sorted(Counter(word1).values())
        freq2 = sorted(Counter(word2).values())

        return freq1 == freq2       