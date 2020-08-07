class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num == 0:
            return 0
        res = 0
        a = 3 if num < 0 else 2
        for i in bin(num)[a:]:
            res += 2 if i == '1' else 1

        return res-1
# return bin(num).count('1') + len(bin(num)) - 3  单行解法
# num = 0的时候，num.bit_length()也等于0。最后结果就变成了-1。我感觉可以改成： return bin(num).count('1') + len(bin(num)) - 3 -3是因为二进制前面有0b两个字符

#  二进制中有0需要1步操作，有1需要2步操作，最后一个1只需要1步。
'''
给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1
错误解法：
var str = num.toString(2);
return str.length + str.replace(/0/g,"").length - 1;

2的次数应该-1,
-1的次数应该包含最高位,
这题结果刚好抵消了.
题目意思不就是数的二进制末尾如果是1(奇)就置0如果是0(偶)就右移(/2),直至变成0,
所以很明显需要右移数的二进制位-1次,有几个1置0几次
'''