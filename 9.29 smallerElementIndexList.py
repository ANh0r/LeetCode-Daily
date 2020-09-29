from typing import List

"""
给定一个列表，返回比当前元素小的元素个数
思路：
根据提示，这个题目要求的数据比较小，所以我们可以建立一个101长度的数据均为0的数组，然后对于原数组里面的每个数据进行计数
看看在数组中出现的次数，拿示例一来说，nums = [8,1,2,2,3] 新计数器数组第8个位置在原数组中出现的次数是1，而第2个位置出现的次数是2
总之每个位置对应该数据出现的次数，最后计算原数组第N个位置的前面N-1项的和就是第N个位置所有小于N的数据个数"""


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic = [0]*101

        for i in nums:
            dic[i] += 1
        print(dic)
        return [sum(dic[0:n]) for n in nums]

t = Solution()
print(t.smallerNumbersThanCurrent([1,1,1,2,2,2,3,3,3,4,4,5,6,7,8,8,9,9]))
"""
方法一：暴力
枚举数组里的每个数字，遍历数组统计有多少数字比当前数字小即可，公式化说，就是对于第 ii 个数字，计算


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        vec = [0] * n
        for i in range(n):
            vec[i] = sum(1 for j in range(n) if nums[j] < nums[i])
        return vec
复杂度分析

时间复杂度：枚举数组里的每个数字为 O(n) ，遍历数组也为 O(n)，所以总时间复杂度为两者相乘，即 O(n 
2
 ) ，其中 n=nums.lengthn=nums.length 。

空间复杂度：O(1)O(1) ，不需要使用额外的空间。

方法二：频次数组 + 前缀和
注意到数字的值域范围为 [0,100][0,100] ，所以可以考虑建立一个频次数组 cnt[i]cnt[i] ，表示数字 ii 出现的次数，那么对于数字 ii 而言，它的答案就是


即小于它的数字出现个数之和，直接算需要遍历 [0,i-1][0,i−1] 的 cntcnt 求和，仍需要线性的时间去计算，但我们注意到这个答案是一个前缀和，所以我们可以再对 cntcnt 数组求前缀和。那么对于数字 ii 的答案就是 cnt[i-1]cnt[i−1] ，算答案的时间复杂度从 O(n)O(n) 降到了 O(1)O(1) 。

最后整个算法流程为：遍历数组元素，更新 cntcnt 数组，即 cnt[nums[i]]+=1 ，然后对 cntcnt 数组求前缀和，最后遍历数组元素，对于相应的数字 O(1)O(1) 得到答案即可。

C++Python

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt, vec = [0] * 101, [0] * n
        for num in nums:
            cnt[num] += 1
        for i in range(1, 101):
            cnt[i] += cnt[i - 1]
        for i in range(n):
            if nums[i]:
                vec[i] = cnt[nums[i] - 1]
        return vec
复杂度分析

时间复杂度：统计 cntcnt 数组的前缀和需要 O(S)O(S) 的时间，遍历数组需要 O(n)O(n) 的时间，所以总时间复杂度为 O(S+n)O(S+n) ，其中 SS 为值域大小，n=nums.lengthn=nums.length 。

空间复杂度：O(S)O(S) ，需要开一个值域大小的数组。

方法三：排序
我们将 numsnums 数组按数字大小从小到大排序，那么对于第 ii 个数字 xx ，数组中在它前面的数字一定小于等于它，而题目要求小于它的数字个数，所以我们可以对于位置 ii 记录一个变量 pre_ipre 
i
​	
  ，表示位置 ii 往前第一个不等于 xx 的数字下标。对于数字 xx ，答案就是 pre_i+1pre 
i
​	
 +1 ，因为数组下标是从 00 开始的，所以需要额外加一。pre_{i}pre 
i
​	
  需要分两种情况更新，如果前面一个数字等于当前数字 xx ，那么 pre_i=pre_{i-1}pre 
i
​	
 =pre 
i−1
​	
  ，否则 pre_i=i-1pre 
i
​	
 =i−1 ，这样即能 O(1)O(1) 推出 pre_ipre 
i
​	
  。

同时注意到 pre_ipre 
i
​	
  只与前一个位置有关，所以可以不用数组存 pre_ipre 
i
​	
  ，直接用一个变量 prepre 表示前一个位置的 pre_{i-1}pre 
i−1
​	
  ，然后不断更新 prepre 即可。

最后整个算法流程为：对每个数字用一个二元组 (number_i,index\ of\ number_i)(number 
i
​	
 ,index of number 
i
​	
 ) 表示数字大小和数字在 numsnums 数组中的下标，用 tmptmp 数组存储所有二元组，按数字 number_inumber 
i
​	
  从小到大排序 tmptmp 数组，最后遍历 tmptmp 数组，按上文说的方法的维护 prepre 变量，对于 tmptmp 数组里第 ii 个元素的答案，应放在答案数组中的第 index\ of\ number_iindex of number 
i
​	
  个位置里 。

C++Python

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        vec = [0] * n
        tmp = sorted([(nums[i], i) for i in range(n)])
        
        pre = -1
        for i in range(n):
            if i != 0 and tmp[i][0] != tmp[i - 1][0]:
                pre = i - 1
            vec[tmp[i][1]] = pre + 1
        return vec
"""