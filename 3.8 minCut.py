class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        g = [[True] * n for _ in range(n)]
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]
        f = [0] * n
        for i in range(n):
            if not g[0][i]:
                f[i] = min(f[j] + 1 for j in range(i) if g[j + 1][i])
        return f[-1]