class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        for n in arr:
            prefix += [prefix[-1] ^ n]
        res = []
        for i, j in queries:
            res += [prefix[j + 1] ^ prefix[i]]
        return res