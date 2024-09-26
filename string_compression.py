from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            char = chars[i]
            group_length = 1
            while i + group_length < len(chars) and chars[i + group_length] == char:
                group_length += 1
            chars[res] = char
            res += 1
            if group_length > 1:
                for digit in str(group_length):
                    chars[res] = digit
                    res += 1
            i += group_length
        return res