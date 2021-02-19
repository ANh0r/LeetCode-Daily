class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        # 维护一个窗口以及zero_nums
        # 若当前窗口中0的个数 zero_nums>K 则 左指针i+1，并且若A[i]==0,左指针在移动的同时zero_nums-1
        # 遍历一次后 窗口自然大小就是最大长度
        n = len(A)
        i,zero_num=0,0
        for j in range(n):
            if A[j]==0:
                zero_num+=1
            if zero_num>K:
                if A[i]==0:
                    zero_num-=1
                i+=1
        return j-i+1