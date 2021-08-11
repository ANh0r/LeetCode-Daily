class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        from collections import defaultdict
        import bisect
        n = len(A)
        lookup = defaultdict(list)
        dp = [defaultdict(int) for _ in range(n)]
        res = 0
        # 记录每个元素的位置
        for idx, val in enumerate(A):
            lookup[val].append(idx)
        for i in range(n):
            for j in range(i):
                diff = A[i] - A[j]
                target = A[j] - diff
                # 先找 和 A[j], A[i]组成三个数组个数
                # for idx in lookup[target]:
                #     if idx < j:
                #         dp[i][diff] += 1
                #     else:
                #         break
                dp[i][diff] += bisect.bisect_left(lookup[target], j) # 可以用二分找个数
                # 加上 第j位置公差为diff个数
                dp[i][diff] += dp[j][diff]
            # 统计个数
            for val in dp[i].values():
                res += val
        return res