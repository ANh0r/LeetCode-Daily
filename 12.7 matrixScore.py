class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        for i in range(len(A)):
            if A[i][0]==0:
                A[i]=[1-tmp for tmp in A[i]]
            # 列变换
            for j in range(1,len(A[0])):
                #每列1的个数比0少才变换
                cnt1=sum(A[i][j] for i in range(len(A)))
                if cnt1<len(A)/2:
                    for i in range(len(A)):
                        A[i][j]=0 if A[i][j] else 1
        # 计算得分
        res=0
        for i in range(len(A)):
            t=A[i][::-1]
            item=[val*2**inx for inx,val in zip(range(len(t)),t)]
            res=res+sum(item)
        return int(res)