class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        preSum = [0]
        presum_index = {0:[-1,-1]}
        for i in range(len(nums)):
            preSum.append(preSum[i]+nums[i] if nums[i] == 1 else preSum[i]+nums[i]-1)
            presum_index[preSum[-1]] = presum_index.get(preSum[-1],[i,i])
            presum_index[preSum[-1]][1] = i
        res = 0
        for v in presum_index.values():
            res = max(v[1] - v[0],res)
        return res