class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def can(start):
            new_gas = gas[start:] + gas[:start]
            new_cost = cost[start:] + cost[:start]
            surplus = 0
            for g, c in zip(new_gas, new_cost):
                # print(start, ' 号加油站, 当前油箱 ', surplus, ', 加油 ', g, ', 下次需花费 ', c, ', 是否可行: ', surplus + g >= c)
                if surplus + g < c:
                    return False
                surplus = surplus + g - c
                start = (start + 1) % len(gas)
            return True

        # 穷举
        for i in range(len(gas)):
            if can(i):
                return i
        return -1