from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(sum(nums[:i+1]))
        return ans


t = Solution()
print((t.runningSum([1,2,3,4,5])))