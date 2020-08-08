class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        zq = max(candies)
        return [i+extraCandies >= zq for i in candies]