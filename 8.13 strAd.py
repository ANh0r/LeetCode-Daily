class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            # print(n1)
            # print(n2)
            # print(tmp)
            carry = tmp // 10
            # print(carry)
            res = str(tmp % 10) + res
            # print(res)
            i, j = i - 1, j - 1
        return "1" + res if carry else res


t = Solution()
print(t.addStrings("11123","111"))
'''算法流程： 设定 i，j 两指针分别指向 num1，num2 尾部，模拟人工加法；

计算进位： 计算 carry = tmp // 10，代表当前位相加是否产生进位；
添加当前位： 计算 tmp = n1 + n2 + carry，并将当前位 tmp % 10 添加至 res 头部；
索引溢出处理： 当指针 i或j 走过数字首部后，给 n1，n2 赋值为 00，相当于给 num1，num2 中长度较短的数字前面填 00，以便后续计算。
当遍历完 num1，num2 后跳出循环，并根据 carry 值决定是否在头部添加进位 11，最终返回 res 即可。
复杂度分析：

时间复杂度 O(max(M,N))O(max(M,N))：其中 MM，NN 为 22 数字长度，按位遍历一遍数字（以较长的数字为准）；
空间复杂度 O(1)O(1)：指针与变量使用常数大小空间。
'''