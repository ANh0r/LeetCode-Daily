class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        q, d = [], {x: i for i, x in enumerate(target)}
        for x in arr:
            if x in d:
                i = bisect_left(q, d[x])
                q[i:i+1] = d[x],
        return len(target) - len(q)