class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        fail = [-1] * n
        for i in range(1, n):
            j = fail[i - 1]
            while j != -1 and s[j + 1] != s[i]:
                j = fail[j]
            if s[j + 1] == s[i]:
                fail[i] = j + 1

        best = -1
        for i in range(n - 1, -1, -1):
            while best != -1 and s[best + 1] != s[i]:
                best = fail[best]
            if s[best + 1] == s[i]:
                best += 1

        add = ("" if best == n - 1 else s[best + 1:])
        return add[::-1] + s


'''kmp:
'''
"""
给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

示例 1:

输入: "aacecaaa"
输出: "aaacecaaa"
示例 2:

输入: "abcd"
输出: "dcbabcd"

思路：
设原字符串为S,则必有H = S'+S是回文字符串，其中S'是S去掉首位的逆序字符串
若令H最短，则需要S'最短，S'是S去掉首位的逆序字符串，因此如果要满足H回文且最短，需要满足
1.S'最短
2.S去掉首位或者首几位，去掉的字符串仍为回文串
3.S去掉包含首位的回文子串后，剩下的字符串逆序为S'
4.去掉的回文串越长，S'越短

于是，此题就变成了如何在一个字符串，从首位开始找到最长回文前缀，之后就是逆序和拼接的事情了

1.kmp next数组找到前缀的index
2.逆序后半部分
3.拼接原字符串
def longest_palindrome_prefix(s):
            if not s:
                return 0
            s = s + '#' + s[::-1] + '$'
            i = 0
            j = -1
            nt = [0] * len(s)
            nt[0] = -1
            while i < len(s) - 1:
                if j == -1 or s[i] == s[j]:
                    i += 1
                    j += 1
                    nt[i] = j
                    # print(nt)
                else:
                    j = nt[j]
                    # print(nt)
            return nt[len(s) - 1]

        def pre_to_ans(s):
            return s[:longest_palindrome_prefix(s)-1:-1]+s
            #[:longest_palindrome_prefix(s)+1]

        return pre_to_ans(s)


"""