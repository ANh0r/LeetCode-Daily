import collections, functools

lookup = collections.defaultdict(list)
steps = collections.defaultdict(int)
# 把所有可以旋转的字符串找出来
for i in range(len(ring)):
    tmp = ring[i:] + ring[:i]
    # 加入以开头字母为键的数组中
    lookup[ring[i]].append(tmp)
    # 距离原始ring顺时针旋转需要几步
    steps[tmp] = i


# 从一个字符串到另一字符串最少旋转的步数
def cal_steps(cur, nxt):
    # return min(tmp: = abs(steps[cur] - steps[nxt]), len(ring) - tmp)

    @functools.lru_cache(None)
    def dfs(cur, k):
        if k == len(key):
            return 0
        res = float("inf")
        for word in lookup[key[k]]:
            res = min(res, cal_steps(cur, word) + 1 + dfs(word, k + 1))
        return res

    return dfs(ring, 0)
"""
视频游戏“辐射4”中，任务“通向自由”要求玩家到达名为“Freedom Trail Ring”的金属表盘，并使用表盘拼写特定关键词才能开门。

给定一个字符串 ring，表示刻在外环上的编码；给定另一个字符串 key，表示需要拼写的关键词。您需要算出能够拼写关键词中所有字符的最少步数。

最初，ring 的第一个字符与12:00方向对齐。您需要顺时针或逆时针旋转 ring 以使 key 的一个字符在 12:00 方向对齐，然后按下中心按钮，以此逐个拼写完 key 中的所有字符。

旋转 ring 拼出 key 字符 key[i] 的阶段中：

您可以将 ring 顺时针或逆时针旋转一个位置，计为1步。旋转的最终目的是将字符串 ring 的一个字符与 12:00 方向对齐，并且这个字符必须等于字符 key[i] 。
如果字符 key[i] 已经对齐到12:00方向，您需要按下中心按钮进行拼写，这也将算作 1 步。按完之后，您可以开始拼写 key 的下一个字符（下一阶段）, 直至完成所有拼写。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/freedom-trail
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""