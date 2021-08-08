class Solution:
    def tribonacci(self, n: int) -> int:
        x = 0
        y = 1
        z = 1

        if n == 0:
            return x
        elif n == 1:
            return y
        elif n == 2:
            return z

        for i in range(3, n+1):
            tmp = x + y + z
            x, y, z = y, z, tmp

        return z