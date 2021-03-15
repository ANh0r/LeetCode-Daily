class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l= [[0 for col in range(n)] for row in range(n)]

        side = [[0,0],[0,n-1],[n-1,n-1],[n-1,0]]    #边角
        way = [[0,1],[1,0],[0,-1],[-1,0]]           #方向
        dire = 0                                    #当前方向
        x = 0                                       #当前纵
        y = 0                                       #当前横

        for i in range(1,n*n+1):
            l[x][y]=i
            nex = (dire+1)%4
            if [x,y]==side[nex]:                    #到边角，换方向
                side[dire][0]+=way[nex][0]
                side[dire][1]+=way[nex][1]
                side[nex][0]+=way[nex][0]
                side[nex][1]+=way[nex][1]
                dire = nex
            x+=way[dire][0]
            y+=way[dire][1]

        return l