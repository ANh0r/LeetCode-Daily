from typing import List
#
#
# class Solution:
#     def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
#         def check(word,pattern):
#             if len(word)!=len(pattern):
#                 return False
#             for i in range(len(word)):
#                 if word.index(word[i])!= pattern.index(pattern[i]):
#                     return False
#             return True
#         res = []
#         for i in range(len(words)):
#             if check(words[i],pattern):
#                 res.append(words[i])
#         return res
#
#
# t = Solution()
# t.findAndReplacePattern(["teast", "love", "yes", "abondon", "tea", "loop", "fiss"],"abcc")
#
# print(t.findAndReplacePattern(["teast","teaa", "love", "yes", "abondon", "tea", "loop", "fiss"],"abcc"))


def check(word, pattern):
    if len(word) != len(pattern):
        return False
    for i in range(len(word)):
        if word.index(word[i]) != pattern.index(pattern[i]):
            return False
    print(word.index((word[i])))
    return True


print(check("love","abcd"))