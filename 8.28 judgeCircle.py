class Solution:
    def judgeCircle(self, moves: str) -> bool:
        sta = [0, 0]
        if not moves:
            return True
        for i in moves:
            if i == 'L':
                sta[0] -= 1
            elif i == 'R':
                sta[0] += 1
            elif i == 'U':
                sta[1] += 1
            elif i == 'D':
                sta[1] -= 1
        return sta == [0, 0]
    # 一行：return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')


t = Solution()
print(t.judgeCircle("RRRRLLLLLUUDD"))



