class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # a = sorted(nums,reverse= True)
        # sum = 1
        # count = 0
        # for i in range (0,3):
        #     sum = sum * int(a[i])
        # return sum
        #升序排序
        nums.sort()
        #计算数组的长度
        a = len(nums)
        #三个数相成的最大值：升序排序后，最后三个数之积（只有正数的情况）；或者最前面两个数与最后一个数的乘积（有负数的情况）
        CumMax = max(nums[a-1]*nums[a-2]*nums[a-3], nums[0]*nums[1]*nums[a-1])
        return CumMax

