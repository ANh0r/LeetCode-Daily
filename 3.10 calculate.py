class Solution:
    def calculate(self, s: str) -> int:
        que = deque()
        for i in s:
            if i!=' ':
                if i==')':
                    eq = ''
                    # py3.8 海象妙用
                    while (t:=que.pop())!='(':
                        eq =t+eq
                    que.append(str(eval(eq)))
                else:
                    que.append(i)
        return eval("".join(que))