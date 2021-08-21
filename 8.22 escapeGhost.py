class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        source = [0, 0]
        distance = manhattanDistance(source, target)
        return all(manhattanDistance(ghost, target) > distance for ghost in ghosts)

def manhattanDistance(point1: List[int], point2: List[int]) -> int:
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])