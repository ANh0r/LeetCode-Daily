class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        width = sum(wall[0])
        height = len(wall)
        counts = collections.defaultdict(lambda : height)
        for row in wall:
            _sum = 0
            for r in row[:-1]:
                _sum += r
                counts[_sum] -= 1

        if len(counts.values()):
            return min(counts.values())
        else:
            return height