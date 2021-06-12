class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # 一个 cost[i] 和 str(i + 1) 对应的dict
        # 如果存在相同cost，只保留后面的str(i + 1)
        d = dict((v, str(i + 1)) for i, v in enumerate(cost))

        # 根据cost[i] 对应 数位的大小 从小到大排列，下文用到该性质
        cost = sorted(list(d.keys()), key=lambda i: d[i])

        @cache
        def dfs(t):
            if not t:
                return ""
            # 默认返回"0"
            s = "0"
            for c in cost:
                if (
                    t >= c
                    and (res := dfs(t - c)) != "0"
                    # 这里要注意的是
                    # 当res = "" 时， 0 + 1 >= len("0")
                    # 当存在 多个长度相同res时， 更靠后的c对应数位更大，将替换旧s
                    and len(res) + 1 >= len(s)
                ):
                    s = d[c] + res
            return s

        return dfs(target)