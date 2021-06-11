class Solution:
    def numSquares(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        a = 0
        while a**2 <= n:
            b = int((n - a**2)**0.5)
            if a**2 + b**2 == n:
                return (not not a) + (not not b)
            a += 1
        return 3
"""
任何正整数都可以拆分成不超过4个数的平方和 ---> 答案只可能是1,2,3,4
如果一个数最少可以拆成4个数的平方和，则这个数还满足 n = (4^a)*(8b+7) ---> 因此可以先看这个数是否满足上述公式，如果不满足，答案就是1,2,3了
如果这个数本来就是某个数的平方，那么答案就是1，否则答案就只剩2,3了
如果答案是2，即n=a^2+b^2，那么我们可以枚举a，来验证，如果验证通过则答案是2
只能是3
"""