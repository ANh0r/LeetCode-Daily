class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        countOnes = ans = 0
        cnts = Counter({0:1})
        for num in nums:
            countOnes += num
            ans += cnts[countOnes - goal]
            cnts[countOnes] += 1
        return ans