class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word2ch = dict()
        ch2word = dict()
        words = s.split()
        if len(pattern) != len(words):
            return False

        for ch, word in zip(pattern, words):
            if (word in word2ch and word2ch[word] != ch) or (ch in ch2word and ch2word[ch] != word):
                return False
            word2ch[word] = ch
            ch2word[ch] = word

        return True
    """
    arr = s.split()
        if len(pattern) != len(arr):
            return False
            
        d1 = {}    # d1 -> 字符为键，单词为值；d2 反之
        d2 = {}

        for i, ch in enumerate(pattern):
            if ch in d1 and d1[ch] != arr[i]:
                return False
            elif arr[i] in d2 and d2[arr[i]] != ch:
                return False
            else:
                d1[ch] = arr[i]
                d2[arr[i]] = ch
        else:
            return True
            """