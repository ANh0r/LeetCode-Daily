class Solution:
    def countBits(self, num: int) -> List[int]:
        def CountOnes(i):
            ones = 0
            while i > 0:
                i &= (i - 1)
                ones = ones + 1
            return ones

        ans = [CountOnes(i) for i in range(num + 1)]
        print(ans)
        return ans

"""
位运算，返回0-num之间每个数的二进制的1的个数
"""
"""
result = [0] * (num + 1)
        for i in range(1, num+1):
            result[i] = result[i//2] + (i&1)
        return result
"""
