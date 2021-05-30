class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0
"""构造掩码，奇数位为1为4的幂，即保证了在2的幂的基础上成为4的幂"""