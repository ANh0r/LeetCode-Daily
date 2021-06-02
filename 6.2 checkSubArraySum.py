class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash_set = set()
        preSum = [nums[0] % k]
        for i in range(1, len(nums)):
            preSum.append((preSum[i - 1] + nums[i]) % k)
            if preSum[i] in hash_set or preSum[i] % k == 0:
                return True
            hash_set.add(preSum[i - 1])

        return False