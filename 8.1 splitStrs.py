class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:]+s[:n]


'''
输入: s = "abcdefg", k = 2
输出: "cdefgab"
'''