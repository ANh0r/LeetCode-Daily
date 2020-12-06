class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i - 1][j] + ret[i - 1][j - 1])
            ret.append(row)
        return ret



"""
        class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]*i for i in range(1,numRows+1)]
        for i in range(2,numRows) :
            for j in range(1,i) :
                ans[i][j] = ans[i-1][j-1]+ans[i-1][j]
        return ans
"""