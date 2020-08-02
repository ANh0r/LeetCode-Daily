class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for num, word in enumerate(sentence.split(), 1):
            if word.startswith(searchWord):
                return num
        return -1


t = Solution()
print(t.isPrefixOfWord('Wo ai nikkkl sb','ni'))