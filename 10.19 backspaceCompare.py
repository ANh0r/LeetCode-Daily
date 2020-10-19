class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        def delback(Stt):
            ans = []
            for i in range(len(Stt)):
                if Stt[i] != '#':
                    ans.append(Stt[i])
                elif Stt[i] == '#' and ans != []:
                    ans.pop()
            return ans

        if delback(S) == delback(T):
            return True
        return False