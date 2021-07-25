class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d = collections.defaultdict(list)
        for a, b in adjacentPairs:
            d[a].append(b)
            d[b].append(a)
        for k in d:
            if len(d[k]) == 1:
                head = k
                break
        last = head
        cur = d[head][0]
        ans = [head, cur]
        while len(d[cur]) > 1:
            last, cur = cur, (d[cur][0] if d[cur][0] != last else d[cur][1])
            ans.append(cur)
        return ans