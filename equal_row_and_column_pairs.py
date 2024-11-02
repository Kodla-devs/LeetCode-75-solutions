from typing import Counter, List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        column_counts = Counter(zip(*grid))

        row_counts = Counter(map(tuple, grid))

        equal_pairs = sum(column_counts[col] * row_counts[col] for col in column_counts)

        return equal_pairs