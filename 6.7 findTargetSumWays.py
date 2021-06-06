class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(i: int, t: int) -> int:
            if i == len(nums):
                return 1 if t == 0 else 0
            return dfs(i + 1, t - nums[i]) + dfs(i + 1, t + nums[i])

        return dfs(0, target)
"""
if not nums or sum(nums) < target or (sum(nums) + target)%2 == 1:
            return 0

        s = (sum(nums)+target)//2 #只一个子集，使得子集和为s

        # 对于每一个数都有加入和不加入两种情况，因此可以使用背包问题的方法求解
        marp = [0 for _ in range(s+1)]
        marp[0] = 1 #当i - num =0也就是这个数加入/不加入正好可以满足要求时，解法为1（这个地方确实想了很久，看了题解）
        for num in nums:
            for i in range(s,num-1,-1):#参考背包问题的自顶向下
                marp[i] = marp[i]+marp[i - num]

        return marp[-1]
"""