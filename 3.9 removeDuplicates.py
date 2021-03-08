class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for i in S:
            if not stack or stack[-1] != i:
                stack.append(i)
            else:
                stack.pop()
        return ''.join(stack)