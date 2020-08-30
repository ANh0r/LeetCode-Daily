class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(i[::-1] for i in s.split(" "))


t = Solution()
print(t.reverseWords("ZhangQi is a SB"))