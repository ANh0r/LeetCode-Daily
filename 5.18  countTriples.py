from collections import defaultdict
class Solution:
    def countTriplets(self, arr) -> int:
        D=defaultdict(list)  #键不存在会自动创建D[*]=list()
        D[0]=[-1]  #xor[-1]=0
        xor=0   #xor[i]=arr[0]^arr[1]^...^arr[i]，xor是概念xor[]的最新值
        for i,a in enumerate(arr):
            xor ^= a        #设D[bit]=数组A，
            D[xor].append(i)#数组A的任意元素i满足xor[i]=bit
        ans=0
        for A in D.values():
            sum=A.copy()   #求A的前缀和数组，注意:sum[0]=A[0]
            for i in range(1,len(sum)): sum[i]+=sum[i-1]
            e=len(A)-1
            for b in range(e):
                ans += sum[e]-sum[b]-(e-b)*(A[b]+1)
        return ans