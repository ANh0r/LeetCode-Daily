class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = list(str(n))
        p, s = 1, 0
        for a in n:
            p *= int(a)
            s += int(a)
        return p - s

