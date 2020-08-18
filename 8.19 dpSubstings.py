class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True

        for r in range(len(s)):
            for l in range(r + 1):
                if s[r] == s[l] and (r - l < 3 or dp[l + 1][r - 1]):
                    dp[l][r] = True

        ans = [0 for _ in range(len(s))]

        for r in range(len(s)):
            for l in range(r + 1):
                if dp[l][r]:
                    ans[r] += 1

        return sum(ans)
'''
先判定s[i][j] 是不是回文串
然后dp[j] 表示以j结尾的回文串的个数  他就是  sum([check[i][j] for i in range(j+1)])
最后sum(dp)即可

作者：linln1-u
链接：https://leetcode-cn.com/problems/palindromic-substrings/solution/er-ci-dong-gui-by-linln1-u/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''