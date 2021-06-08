class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_num = sum(stones)
        marp = [0 for _ in range(sum_num // 2 + 1)]

        for i in range(len(stones)):
            for j in range(sum_num // 2, stones[i] - 1, -1):
                marp[j] = max(marp[j], marp[j - stones[i]] + stones[i])

        return sum_num - 2 * marp[-1]