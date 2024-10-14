import collections
import bisect

class Solution:
    def preprocess_t(self, t: str):
        char_indices = collections.defaultdict(list)
        for index, char in enumerate(t):
            char_indices[char].append(index)
        return char_indices

    def isSubsequence(self, s: str, t: str) -> bool:
        char_indices = self.preprocess_t(t)
        
        current_position = -1
        
        for char in s:
            if char not in char_indices:
                return False
            indices = char_indices[char]
            i = bisect.bisect_right(indices, current_position)
            if i == len(indices):
                return False
            current_position = indices[i]
        
        return True