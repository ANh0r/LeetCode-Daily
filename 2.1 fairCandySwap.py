class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sumA, sumB = sum(A), sum(B)
        delta = (sumA - sumB) // 2
        rec = set(A)
        ans = None
        for y in B:
            x = y + delta
            if x in rec:
                ans = [x, y]
                break
        return ans