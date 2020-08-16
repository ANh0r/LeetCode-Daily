class MagicDictionary(object):
    def __init__(self):
        self.buckets = collections.defaultdict(list)

    def buildDict(self, words):
        for word in words:
            self.buckets[len(word)].append(word)

    def search(self, word):
        return any(sum(a!=b for a,b in zip(word, candidate)) == 1
                   for candidate in self.buckets[len(word)])


class MagicDictionary2:
    class MagicDictionary(object):
        def __init__(self):
            self.buckets = collections.defaultdict(list)

    def buildDict(self, words):
        for word in words:
            self.buckets[len(word)].append(word)

    def search(self, word):
        return any(sum(a != b for a, b in zip(word, candidate)) == 1
                   for candidate in self.buckets[len(word)])


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
'''

实现一个带有buildDict, 以及 search方法的魔法字典。

对于buildDict方法，你将被给定一串不重复的单词来构建一个字典。

对于search方法，你将被给定一个单词，并且判定能否只将这个单词中一个字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。

示例 1:

Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-magic-dictionary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



如果一个字符中只有一个字符可以更改，即它们的汉明距离为 1。
在搜索新单词时，我们只检查长度相同的单词。'''

'''复杂度分析

时间复杂度：O(S)O(S) 构建和 O(NK)O(NK) 搜索，其中 NN 是魔法字典中的单词数，SS 是其中的字母总数，KK 是搜索单词的长度。
空间复杂度：O(S)O(S)。
方法二：广义邻居
回想一下，在方法 1 中，如果一个单词中只有一个字符可以更改以使字符串相等，那么两个单词就是邻居。

让我们假设一个词 “apple” 具有广义邻居 “pple”、“aple”、“aple”、“appe” 和 “appl”。在搜索像 apply 这样的词是否有像 apple 这样的邻居时，我们只需要知道它们是否有一个广义邻居。

算法：
继续上述思考，一个问题是 “apply” 不是自身的邻居，而是具有相同的广义邻居 “*pply”。为了解决这个问题，我们将计算生成 “*pply” 的源的数量。如果有 2 个或更多，则其中一个不会是 “apply”。如果只有一个，我们应该检查它不是 “apply”。无论是哪种情况，我们都可以确定有一些神奇的单词生成了 “*pply”，而不是 “apply”。

Python

class MagicDictionary(object):
    def _genneighbors(self, word):
        for i in xrange(len(word)):
            yield word[:i] + '*' + word[i+1:]

    def buildDict(self, words):
        self.words = set(words)
        self.count = collections.Counter(nei for word in words
                                        for nei in self._genneighbors(word))

    def search(self, word):
        return any(self.count[nei] > 1 or
                   self.count[nei] == 1 and word not in self.words
                   for nei in self._genneighbors(word))
'''