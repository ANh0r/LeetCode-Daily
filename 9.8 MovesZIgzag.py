"""

给你一个整数数组 nums，每次 操作 会从中选择一个元素并 将该元素的值减少 1。

如果符合下列情况之一，则数组 A 就是 锯齿数组：

每个偶数索引对应的元素都大于相邻的元素，即 A[0] > A[1] < A[2] > A[3] < A[4] > ...
或者，每个奇数索引对应的元素都大于相邻的元素，即 A[0] < A[1] > A[2] < A[3] > A[4] < ...
返回将数组 nums 转换为锯齿数组所需的最小操作次数。

 

示例 1：

输入：nums = [1,2,3]
输出：2
解释：我们可以把 2 递减到 0，或把 3 递减到 1。

此处输出2是因为 2-0 = 2 以及 3-1 = 2


示例 2：

输入：nums = [9,6,1,6,2]
输出：4

9-5 = 4 仅需要把 9减少到5即可

思路：
因为本题只能减少 不能增加，所以判断锯齿只需要将要判断位置减少到比相邻位置小即可
1.判断
① nums[i]>nums[i+1]或者nums[i]>nums[i-1]需要计算相邻差值 否则不需要累加
对边界进行二次判断
② 对于奇偶同样判断，结果取小

"""
from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        ans1 = 0
        ans2 = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                d1 = nums[i] - nums[i-1] + 1 if i > 0 and nums[i] >= nums[i-1] else 0
                d2 = nums[i] - nums[i+1] + 1 if i < len(nums)-1 and nums[i] >= nums[i+1] else 0
                ans1 += max(d1, d2)
            else:
                d1 = nums[i] - nums[i - 1] + 1 if nums[i] >= nums[i - 1] else 0
                d2 = nums[i] - nums[i + 1] + 1 if i < len(nums) - 1 and nums[i] >= nums[i + 1] else 0
                ans2 += max(d1, d2)
        return min(ans1,ans2)


t = Solution()
print(t.movesToMakeZigzag([0,2,0]))



''' 
        n,ans=len(nums),[0,0]
        for k in range(2):
            for i in range(k,n,2):
                d = 0
                if i > 0:
                    d = max(d,nums[i]-nums[i-1]+1)
                if i+1 < n:
                    d = max(d,nums[i]-nums[i+1]+1)
                ans[k] += d
        return min(ans)'''










