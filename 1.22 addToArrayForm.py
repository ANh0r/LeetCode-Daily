class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        ans = ''
        for i in A:
            ans += str(i)
        ans = int(ans)+K
        return list(str(ans))
