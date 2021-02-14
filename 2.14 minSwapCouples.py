class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        """
        每两个座位成一对，假定左边的人都是合法的不变，如果TA右边的人与TA匹配则
        跳过，不匹配则找到TA的匹配对象的与TA右边的人交换。
        """
        def find_another(n):
            if n % 2 == 0:
                return n + 1
            else:
                return n - 1

        c = 0
        for i in range(0, len(row), 2):
            p1 = row[i]
            p2 = find_another(p1)
            if row[i+1] != p2:
                j = row.index(p2)
                row[i+1], row[j] = row[j], row[i+1]
                c += 1
        return c
"""
N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手。 计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。 一次交换可选择任意两人，让他们站起来交换座位。

人和座位用 0 到 2N-1 的整数表示，情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2N-2, 2N-1)。

这些情侣的初始座位  row[i] 是由最初始坐在第 i 个座位上的人决定的。

示例 1:

输入: row = [0, 2, 1, 3]
输出: 1
解释: 我们只需要交换row[1]和row[2]的位置即可。
示例 2:

输入: row = [3, 2, 0, 1]
输出: 0
解释: 无需交换座位，所有的情侣都已经可以手牵手了。

"""