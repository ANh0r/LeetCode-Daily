class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # 最小值得是任何一个货物都可以运走, 不可以分割货物
        start = max(weights)
        # 最大值是一趟就全部运走, 所以是所有货物之和
        end = sum(weights)
        # 二分法模板
        while start < end:
            # 先求中间值
            mid = (start + end)//2

            # 计算这个中间值需要计算需要多少天运完
            days = self.countDays(mid, weights)
            # 如果天数超了, 说明运载能力有待提升, start改大一点, 继续二分搜索
            if days > D:
                start = mid + 1
            # 否则运载能力改小一点继续搜索
            else:
                end = mid
        return start

    def countDays(self, targetWeight, weights):
        days = 1
        i = 0
        current = 0
        for weight in weights:
            current += weight
            if current > targetWeight:
                days += 1
                current = weight
        return days