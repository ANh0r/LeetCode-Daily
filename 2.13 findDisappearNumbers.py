class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        将范围内数组的所有数字当做是否为正数的flag，如果给定数组在范围内则对应位置的数组值为负数，反之则为正数
        举例：给定1~5,给定数组[2，3，4，3，1]
        则对于1~5所有数字来说[-2,-3,-4,-3,1]
        5没有出现在给定数组，所以index = 5处仍然是正数
        return 5
        """
        for num in nums:
            nums[abs(num)-1] = -abs(nums[abs(num)-1])
            # num :数组中给定的下标 nums[num] :对应的值
        print(nums)
        return [i+1 for i,num in enumerate(nums) if num > 0]
"""
n = len(nums)
obj = range(1,(n+1))
return list(set(obj) - set(nums))
"""