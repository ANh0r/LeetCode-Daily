class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count("1")
        res = 0
        while n:
            res += n&1
            n = n >> 1
        return res
t = Solution()
print(t.hammingWeight(1))
