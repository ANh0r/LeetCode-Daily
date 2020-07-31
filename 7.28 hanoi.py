class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """

        def hanoi(n, x, y, z):
            if n == 1:
                z.append(x.pop())
                return
            else:
                hanoi(n - 1, x, z, y)
                hanoi(1, x, y, z)
                hanoi(n - 1, y, x, z)

        hanoi(len(A), A, B, C)

        
'''
注意：hanoi(n, x, y, z)
代表将x柱上的n个盘，借助y柱移动到z柱上。

返回值只需要空就行，这题只是把A的盘全部转移到C盘上，所以Python使用一行代码C[:] = A[:]
都能过。

当A只有一个盘的时候，我们需要将A的最后一个盘取出，放到C上，即C.append(A.pop())，此时A盘空，返回即可，这里也是我们的递归终止条件。

然后当A不是一个盘的时候（可以是n != 1
即else，也可以是n != 0，其实是一样的），就需要进行递归主体的设计了。

我们将A柱除最下面的盘外的所有盘视为一个整体：
hanoi(n - 1, x, z, y)
首先将x柱上的n - 1
个盘，借助z柱移动到y柱上，
hanoi(1, x, y, z)
再将x柱上的1个盘，借助y柱移动到z柱上（这里其实没有用到y柱），
hanoi(n - 1, y, x, z)
最后将y柱上的n - 1
个盘，借助x柱移动到z柱上。

移动完成！

作者：821218213
链接：https: // leetcode - cn.com / problems / hanota - lcci / solution / mian - shi - ti - 0
806 - jiang - di - gui - jin - xing - dao - di - yi - n /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''