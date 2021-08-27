from typing import List

"""def numRescueBoats(self, people: List[int], limit: int) -> int:dist = {}
        for num in people:
            if num not in dist:
                dist[num] = 1
            else:
                dist[num] += 1
        res = 0
        for i in range(len(people)-1, -1, -1):
            a = people[i]
            if dist[a] > 0:
                dist[a] -= 1
            else:
                continue
            b = limit - a
            for j in range(b, -1 ,-1):
                if j in dist and dist[j] > 0:
                    dist[j] -= 1
                    break
            res += 1
        return res
"""

