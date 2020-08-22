from typing import List

#  实数部分给出四个数的列表，求经过四则运算能否得到24
#  共C42 * C32 * C22 8 C12 = 9216种
# 回溯法 ：一种通过探索所有可能的候选解来找出所有的解的算法。
# 如果候选解被确认不是一个解的话（或者至少不是最后一个解），回溯算法会通过在上一步进行一些变化抛弃该解，即回溯并且再次尝试。


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        TARGET = 24
        EPSILON = 1e-6 # 实数部分，可以做小数（浮点数）的计算
        ADD, MULTIPLY, SUBTRACT, DIVIDE = 0, 1, 2, 3  #  给定对应关系
        # 顺序可以将0、1（加、乘）放在一起，代码优化（满足交换律） 少回溯一步

        def solve(nums: List[float]) -> bool:
            if not nums:
                #  回溯完毕 无解
                return False
            if len(nums) == 1:
                #  结果和10^-6对比，精度确认
                return abs(nums[0] - TARGET) < EPSILON
            for i, x in enumerate(nums):
                #  回溯开始
                for j, y in enumerate(nums):
                    if i != j:
                        #  取出两个数，组成列表，此时有C24 ， i和j分别为下标
                        #  在i！= j的情况，即找其他两个元素
                        newNums = list()
                        for k, z in enumerate(nums):
                            if k != i and k != j:
                                newNums.append(z)
                                # 找到了第三个元素
                        for k in range(4):
                            # 四种运算
                            if k < 2 and i > j:
                                # 加法和乘法，代码优化
                                continue
                            # 逐次遍历计算，放入新数组中
                            if k == ADD:
                                newNums.append(x + y)
                            elif k == MULTIPLY:
                                newNums.append(x * y)
                            elif k == SUBTRACT:
                                newNums.append(x - y)
                            elif k == DIVIDE:
                                if abs(y) < EPSILON:
                                    # 除数不为0
                                    continue
                                newNums.append(x / y)
                            if solve(newNums):
                                # 数组内有值，可以继续回溯
                                # 此处是对上述计算之后，判断能否继续进行计算
                                return True
                            newNums.pop()
                            # 添加的结果移除掉，因为回溯枚举时需要去掉第一步回溯时的数
                            # 全排列：当枚举第二位时，第一位出现的数字就不能再次枚举了
                            # 要做到不重不漏
            return False

        return solve(nums)
