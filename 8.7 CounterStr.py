import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sc=collections.Counter(s)
        print(sc)
        tc=collections.Counter(t)
        print(tc)
        return len(list((sc-tc).elements()))

t = Solution()
t.minSteps("qwertttt","asdfertt")