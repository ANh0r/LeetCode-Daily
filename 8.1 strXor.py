class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        strs = [start + 2*i for i in range(0,n)]
        sum = 0
        for i in range (0,len(strs)):
            sum ^= strs[i]
        return sum

# 数组异或