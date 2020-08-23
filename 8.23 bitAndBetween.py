"""
给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。

示例 1: 

输入: [5,7]
输出: 4
示例 2

输入: [0,1]
输出: 0


"""
# 终于有一道看起来我会的题了
# 这个题的由于与操作，所有含有0的位在与操作中最后都会置0，所以实际上在区间[m,n]内对数字进行按按位与实际上是求二进制的公共前缀
# 可以用bit移位操作


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        # 右移位
        while m < n:
            m = m >> 1
            n = n >> 1
            shift = shift + 1
            print("m = "+str(m))
            # print(m)
            print("n = "+str(n))
        return m << shift
        # m 为公共前缀，shift是左移位数，即需要置零的位数


t = Solution()
print(t.rangeBitwiseAnd(2,7))
'''我们的想法是将两个数字不断向右移动，
直到数字相等，即数字被缩减为它们的公共前缀。然后，通过将公共前缀向左移动，
将零添加到公共前缀的右边以获得最终结果。'''

'''Brian Kernighan 算法：还有一个位移相关的算法叫做「Brian Kernighan 算法」，它用于清除二进制串中最右边的 11。

Brian Kernighan 算法的关键在于我们每次对 
相邻两数之间m、m-1进行按位与运算后，m最右边的 1 会被抹去变成 0。

其思想是，对于给定的范围 [m,n]
我们可以对数字 n 迭代地应用上述技巧，清除最右边的 1，
直到它小于或等于 m，此时非公共前缀部分的 1 均被消去。因此最后我们返回 n 即可。

'''


class Solution2:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            # 抹去最右边的 1
            n = n & (n - 1)
        return n
