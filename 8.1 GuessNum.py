from typing import List


class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        sum = 0
        for i in range(3):
            if guess[i] == answer[i]:
                sum += 1
                continue
        return sum


#  面试时候出现这种题就好了
