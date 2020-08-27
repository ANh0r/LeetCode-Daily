from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        conversion={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(digits)==0:
            return []
        product=['']
        # print(product)
        for k in digits:
            print([i+'1' for i in product])
            product=[i+j for i in product for j in conversion[k]]
            print(product)
        return product

t = Solution()
t.letterCombinations("23")

'''优化格式：
f not digits:
            return []
        res = [""]
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        for digit in digits:
            res = [r+char for r in res for char in dic[digit]]
        return res
        '''