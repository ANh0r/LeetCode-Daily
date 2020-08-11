from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)-1):
            if i%2 == 0:
                ans.append(nums[i]*[nums[i+1]])
        zq = []
        for k in range(len(ans)):
            zq += ans[k]
        return zq
'''
ans = []
        tmp = 0
        for i in range(len(nums)):
            if i %2 == 0:
                tmp = nums[i]
            else:
                ans = ans + tmp * [nums[i]]
        return ans
        '''


t =Solution()
print(t.decompressRLElist([1,2,3,4,5,6]))