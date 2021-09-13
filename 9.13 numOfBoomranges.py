class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)):
            hash_map = defaultdict(int)
            for j in range(len(points)):
                if i == j :
                    continue
                x,y = points[i][0]-points[j][0], points[i][1]-points[j][1]
                dist = x**2+y**2
                hash_map[dist] += 1
            for k in hash_map.values():
                ans += k*(k-1)
        return ans