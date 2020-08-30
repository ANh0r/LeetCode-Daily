"""给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

示例 1:

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
"""
from typing import List

"""思路:
第一次简历：
从前向后遍历，保存到当前位置为止的最大值，若下个数大于等于max_num，则更新max_num。否则，更新需要排序数组的右界right。

初始化right=0，max_num=nums[0]
遍历数组，遍历区间0,n)：
若nums[i]>=max_num，更新max_num=nums[i]
否则，更新右界right=i
第二次简历：
从后向前遍历，使用min_num，保存到当前位置为止的最小值，若下个数小于等于min_num，则更新min_num。否则，更新需要排序数组的左界left。

初始化left=n，min_num=nums[−1]
遍历数组，遍历区间(n,0]：
若nums[i]<=min_num，更新min_num=nums[i]
否则，更新左界right=i
若right−left+1>0，返回right−left+1，否则，返回00



"""


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = len(nums)
        if left == 1:
            return 0
        right = 0
        max_num = nums[0]
        min_num = nums[-1]
        for i in range(len(nums)):
            if nums[i] >= max_num:
                max_num = nums[i]
            else:
                right = i
        for i in range(len(nums)-1,-1,-1):
            # print(i)
            if nums[i] <= min_num:
                min_num = nums[i]
                print("minnum = ")
                print(min_num)
                print("i = ")
                print(i)
            else:
                left = i
        print(right)
        print(left)
        return right - left + 1 if (right - left + 1 > 0) else 0

t = Solution()
print(t.findUnsortedSubarray([1,3,2,3,3]))

