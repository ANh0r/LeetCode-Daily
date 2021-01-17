class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # flag=True
        # for i in range(len(coordinates)-2):
        #     k1=(coordinates[i][1]-coordinates[i+1][1])*(coordinates[i+1][0]-coordinates[i+2][0])
        #     k2=(coordinates[i+1][1]-coordinates[i+2][1])*(coordinates[i][0]-coordinates[i+1][0])
        #     if k1!=k2:
        #         flag=False
        #         break
        # return flag
        if coordinates is None or len(coordinates) <= 2:
            return True

        dy = coordinates[1][1] - coordinates[0][1]
        dx = coordinates[1][0] - coordinates[0][0]

        for i in range(2, len(coordinates)):
            dy1 = coordinates[i][1] - coordinates[0][1]
            dx1 = coordinates[i][0] - coordinates[0][0]
            if dy * dx1 != dy1 * dx:
                return False

        return True
"""
判断给的点是不是在同一条直线
"""