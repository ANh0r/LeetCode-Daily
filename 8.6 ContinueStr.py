class Solution:
    def maxPower(self, s: str) -> int:
        ans = 1
        length = 0
        before = ''
        for i in range(len(s)):
            if i == 0:
                before = s[i]
                length = 1
            else:
                if before == s[i]:
                    length += 1

                else:
                    length = 1
                    before = s[i]
            ans = max(ans, length)
        return ans

t = Solution()
print(t.maxPower("asdfghjkl"))