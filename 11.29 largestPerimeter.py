class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        # i=0
        # A.sort(reverse=True)
        # while i<len(A)-2:
        #     if A[i]<A[i+1]+A[i+2]:return A[i]+A[i+1]+A[i+2]
        #     i+=1
        # return 0
        # A = [1, 3]
        length = len(A)
        if length < 3:
            return 0
        A.sort(reverse=True)
        for i in range(length - 2):
            a = A[i]
            b = A[i + 1]
            c = A[i + 2]
            if a - c < b and b + c > a:
                return a + b + c
        return 0
    """
    构成三角形的最大周长
    input:List
    Output:int
    method:
    1.大到小排序
    2.两边之和大于第三边-> 第二大和第三大的大于最大边
    3.两边之差小于第三边-> 最大差值存在于最大和最小的边作差
    """