from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table =set()
        for num in nums:
            if target - num in hash_table:
                return [num,target-num]
            hash_table.add(num)
        return -1




t = Solution()
print(t.twoSum([1,1,1,1],2))