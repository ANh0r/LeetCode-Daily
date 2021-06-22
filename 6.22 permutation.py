class Solution:
    def permutation(self, s: str) -> List[str]:
        def dfs(s, path):
            if not s:
                res.append(path)
                return
            seen = 0
            for i, c in enumerate(s):
                if not seen>>(ord(c)-ord('a')) & 1:
                    seen |= (1<<(ord(c)-ord('a')))
                    dfs(s[:i]+s[i+1:], path+c)
        res = []
        dfs(s, "")
        return res