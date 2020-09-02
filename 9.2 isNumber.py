"""请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，
 但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

 思路：
 1.搞事情思路
 Python 的异常捕获机制用来判断输入的是否为数值
 try :
    float(s)
expect ValueError:
    return False
return True

2.正常题解
有限自动状态机

开始的空格
幂符号前的正负号
小数点前的数字
小数点、小数点后的数字
当小数点前为空格时，小数点、小数点后的数字
幂符号
幂符号后的正负号
幂符号后的数字
结尾的空格

算法流程：
初始化：

状态转移表 states ： 设states[i] ，其中 i 为所处状态，states[i] 使用哈希表存储可转移至的状态。键值对(key,value) 含义：
若输入 key ，则可从状态 i 转移至状态 value 。
当前状态 p ： 起始状态初始化为p=0 。
状态转移循环： 遍历字符串 s 的每个字符 c 。

记录字符类型 t ： 分为四种情况。
当 c 为正负号时，执行 t = 's' ;
当 c 为数字时，执行 t = 'd' ;
当 c 为 e , E 时，执行 t = 'e' ;
当 c 为 . , 空格 时，执行 t = c （即用字符本身表示字符类型）;
否则，执行 t = '?' ，代表为不属于判断范围的非法字符，后续直接返回 false 。
终止条件： 若字符类型 t 不在哈希表 states[p] 中，说明无法转移至下一状态，因此直接返回 False 。
状态转移： 状态 pp 转移至 states[p][t] 。
返回值： 跳出循环后，若状态p∈2,3,7,8 ，说明结尾合法，返回True ，否则返回False 。

复杂度分析：
时间复杂度 O(N)O(N) ： 其中 N 为字符串s 的长度，判断需遍历字符串，每轮状态转移的使用 O(1) 时间。
空间复杂度 O(1)O(1) ： states 和 p 使用常数大小的额外空间。


"""
class Solution:
    def isNumber(self, s: str) -> bool:
        states = [
            { ' ': 0, 's': 1, 'd': 2, '.': 4 }, # 0. start with 'blank'
            { 'd': 2, '.': 4 } ,                # 1. 'sign' before 'e'
            { 'd': 2, '.': 3, 'e': 5, ' ': 8 }, # 2. 'digit' before 'dot'
            { 'd': 3, 'e': 5, ' ': 8 },         # 3. 'digit' after 'dot'
            { 'd': 3 },                         # 4. 'digit' after 'dot' (‘blank’ before 'dot')
            { 's': 6, 'd': 7 },                 # 5. 'e'
            { 'd': 7 },                         # 6. 'sign' after 'e'
            { 'd': 7, ' ': 8 },                 # 7. 'digit' after 'e'
            { ' ': 8 }                          # 8. end with 'blank'
        ]
        p = 0                           # start with state 0
        for c in s:
            if '0' <= c <= '9': t = 'd' # digit
            elif c in "+-": t = 's'     # sign
            elif c in "eE": t = 'e'     # e or E
            elif c in ". ": t = c       # dot, blank
            else: t = '?'               # unknown
            if t not in states[p]: return False
            p = states[p][t]
        return p in (2, 3, 7, 8)
