from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:  # 递归终止条件
            return [nums]
        res = []
        for idx, num in enumerate(nums):
            res_nums = nums[:idx] + nums[idx + 1:]  # 确定剩余元素
            print("res_nums:")
            print(res_nums)
            for j in self.permute(res_nums):
                res.append([num] + j)
                print('res = ')
                print(res)
        return res

t =Solution()
t.permute([1,2,3])