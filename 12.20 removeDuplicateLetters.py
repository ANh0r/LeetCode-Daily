class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnts = collections.Counter(s)
        exists, stack = set(), []
        for c in s:
            if c not in exists:
                while stack and stack[-1] > c and cnts[stack[-1]] > 0:
                    exists.remove(stack.pop())
                exists.add(c)
                stack.append(c)
            cnts[c] -= 1
        return ''.join(stack)
"""
que = []
for i, c in enumerate(s):
    if c in que:  # c已在栈内，由于是递增栈，无需替换c的位置
        continue
    while que and c < que[-1] and que[-1] in set(s[i:]):
        que.pop()
    que.append(c)
return ''.join(que)
"""