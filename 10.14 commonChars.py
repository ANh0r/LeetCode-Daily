import collections
from typing import List
from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        m = collections.Counter(A[0])
        for a in A[1:]:
            m &= collections.Counter(a)
        return m.elements()

    ''' if not A:
            return []

        res = []
        for c in set(A[0]):
            count = [w.count(c) for w in A]
            s = c * min(count)  # 如果不是每个单词都有的字母，min(count)=0
            # for a in s:
            res += s
        return res'''

t = Solution()
print(t.commonChars(['abb','baa']))


