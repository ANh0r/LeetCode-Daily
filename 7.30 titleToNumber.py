class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        #26进制转10进制
        ans = 0
        for x in columnTitle:
            ans *= 26
            ans += ord(x)-ord('A')+1 # A为1
        return ans