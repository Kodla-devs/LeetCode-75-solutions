class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)

        result = []

        for candy in candies:
            result.append(candy + extraCandies >= maxCandies)
        
        return result
        