class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1,1]
        else:
            res=[1]
            back=self.getRow(rowIndex-1)
            n=len(back)
            for i in range(n-1):
                res.append(back[i]+back[i+1])
            res.append(1)
            return res
        # """
        # :type rowIndex: int
        # :rtype: List[int]
        # """
        # res = [[1 for j in range(i + 1)] for i in range(rowIndex + 1)]
        # for i in range(2, rowIndex + 1):
        #     for j in range(1, i):
        #         res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        # return res[-1]

"""
杨辉三角
"""