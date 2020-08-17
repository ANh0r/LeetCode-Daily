class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        res = []
        for word in words:
            w = set(word.lower())
            if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):
                res.append(word)
        return res
'''
issubset() 方法用于判断集合的所有元素是否都包含在指定集合中，如果是则返回 True，否则返回 False。

语法
issubset() 方法语法：

set.issubset(set)

'''