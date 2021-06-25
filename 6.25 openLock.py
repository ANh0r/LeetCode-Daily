class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # deadends转化为set加速in check
        if "0000" in (deadends := set(deadends)):
            return -1
        elif target == "0000":
            return 0

        # BFS由一个 双端队列q 和 一个字典d {存遍历过的字符串: 需要旋转次数}组成，组成namedtuple
        BFS = namedtuple("BFS", "q, d")
        s, e = BFS(deque(["0000"]), {"0000": 0}), BFS(deque([target]), {target: 0})
        while s.q and e.q:
            # 选一个短的q拓展, 降低解空间复杂度
            if len(s.q) > len(e.q):
                s, e = e, s
            for _ in range(len(s.q)):
                c = s.q.popleft()
                for nxt in [
                    # 需要操作的位先转化为int, 加减1后%10，在转化为str，再和剩余位拼接
                    c[:i] + str((int(v) + x) % 10) + c[i + 1 :]
                    for x in (-1, 1)
                    for i, v in enumerate(c)
                ]:
                    # 双向BFS交集，求得解空间
                    if nxt in e.d:
                        return s.d[c] + e.d[nxt] + 1
                    elif nxt not in s.d and nxt not in deadends:
                        s.q.append(nxt)
                        s.d[nxt] = s.d[c] + 1
        return -1