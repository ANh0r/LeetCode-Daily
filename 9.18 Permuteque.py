class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        temp=[]
        def back(nums,temp):
            if not nums:
                res.append(temp)
                return
            else:
                for i in range(len(nums)):
                    if i>0 and nums[i]==nums[i-1]:
                        continue
                    back(nums[:i]+nums[i+1:],temp+[nums[i]]) #这种拼接方法是天然的标记，判断前一字符是否在循环里。
        back(nums,temp)
        return res
"""
剪枝依据是只要在本轮搜索中（图上的同一排）
使用和上一次相同的字符了 那么直接减掉（当然要先排序） 
参考之前46题的做法 其实更容易理解一点 只在剩下的数字里按顺序挑，如果本次选的和上一次的一样 那么后面的直接砍掉。

给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]


"""