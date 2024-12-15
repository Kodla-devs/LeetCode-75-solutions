class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        or_ab = a | b

        mismatch = or_ab ^ c

        flips_for_mismatch = mismatch.bit_count()

        double_flips = (a & b & mismatch).bit_count()

        return flips_for_mismatch + double_flips
        