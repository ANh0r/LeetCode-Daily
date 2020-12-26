class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        nums = [int(''.join(row), base=2) for row in matrix] #先将每一行变成2进制的数字
        ans, N = 0, len(nums)
        for i in range(N):#遍历每一行，求以这一行为第一行的最大矩形
            j, num = i, nums[i]
            while j < N: #依次与下面的行进行与运算。
                num = num & nums[j]  #num中为1的部分，说明上下两行该位置都是1，相当于求矩形的高，高度为j-i+1
                # print('num=',bin(num))
                if not num: #没有1说明没有涉及第i到第j行的竖直矩形
                    break
                width, curnum = 0, num
                while curnum:
                    #将cursum与自己右移一位进行&操作。如果有两个1在一起，那么cursum才为1，相当于求矩形宽度
                    width += 1
                    curnum = curnum & (curnum >> 1)
                    # print('curnum',bin(curnum))
                ans = max(ans, width * (j-i+1))
                # print('i','j','width',i,j,width)
                # print('ans=',ans)
                j += 1
        return ans