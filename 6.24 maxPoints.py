class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)

        def gcd(a, b):
            while b:
                n = a % b
                a = b
                b = n
            return a

        d = {}
        for i in range(0, len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]
                ku, kd = y2 - y1, x2 - x1
                if (x1, y1) != (x2, y2):
                    ku, kd = ku // gcd(ku, kd), kd // gcd(ku, kd)
                d[str(ku) + str(kd) + str(x1) + str(y1)] = d.get(str(ku) + str(kd) + str(x1) + str(y1), 1) + 1
        return max(d.values())