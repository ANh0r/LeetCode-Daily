"""
在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。

注意:
n 是正数且在32位整数范围内 ( n < 231)。

示例 1:

输入:
3

输出:
3
示例 2:

输入:
11

输出:
0

说明:
第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。
1234567891011
"""
class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        bit = 1
        bit_count = 9
        while n > (bit * bit_count):
            n -= bit * bit_count
            bit += 1
            bit_count *= 10
        if n % bit == 0:
            return int(str(10 ** (bit - 1) + n // bit - 1)[-1])
        else:
            return int(str(10 ** (bit - 1) + n // bit)[n % bit - 1])