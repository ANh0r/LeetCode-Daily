class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        preL,preR = 0,0
        n = len(s)
        for i in range(n):
            if s[i] == 'L':
                preL += 1
            else:
                preR += 1
            if preL == preR:
                ans += 1
                preL,preR = 0,0
        return ans