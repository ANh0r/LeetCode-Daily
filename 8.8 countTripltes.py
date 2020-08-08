from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        class Solution:
            def countTriplets(self, arr) -> int:
                ans = 0
                for i in range(len(arr) - 1):  # i<j<=k<len(arr) => i<len(arr)-1
                    xor = arr[i]  # 找满足 arr[i]^arr[i+1]^...^arr[k]的所有(i,k)对
                    for k in range(i + 1, len(arr)):
                        xor ^= arr[k]
                        if 0 == xor: ans += k - i  # i<j<=k ,j有k-i种取值
                return ans




            '''from collections import defaultdict
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

作者：java_Lee
链接：https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/solution/cong-on2dao-onjie-fa-by-java_lee/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''
''' = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
要使得a==b，则 a^b==0，由异或运算的交换律、结合律，则有：
a^b=0 <=> arr[i] ^ arr[i + 1] ^ ... ^ arr[k] == 0 ①
这就意味着，只要找到 i<k 使得上面的①式成立，j取任意满足i<j<=k的值都可以！
利用分析1中的①式子.就可以写出O(N²)的暴力算法了。

作者：java_Lee
链接：https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/solution/cong-on2dao-onjie-fa-by-java_lee/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''

#  [2，3，1，6，4]
'''现需要从数组中取三个下标 i、j 和 k ，其中 (0 <= i < j <= k < arr.length) 。

a 和 b 定义如下：

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
注意：^ 表示 按位异或 操作。

请返回能够令 a == b 成立的三元组 (i, j , k) 的数目

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''