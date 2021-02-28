class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
      #  本题还可以用排序之后和原数组相比是否相同来确定是否是单调数组
      ## 代码： return A == sorted(A) or A == sorted(A,reverse=True)
        up = 0
        de = 0
        for i in range (len(A)-1):
            if A[i] > A[i+1]:
                up = 1
            elif A[i] < A[i+1]:
                de = 1
        return not (up and de)