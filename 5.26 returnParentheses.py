class Solution:
    def reverseParentheses(self, s: str) -> str:
        while '(' in s:
            s = re.sub(r'\(([^()]*)\)', lambda x:x.group(1)[::-1], s)
        return s