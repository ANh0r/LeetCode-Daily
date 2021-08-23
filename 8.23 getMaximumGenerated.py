class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0:
            return 0
        nums=[0,1]
        for i in range(2,n+1):
            if i%2==0:
                nums.append(nums[i//2])
            else:
                nums.append(nums[(i-1)//2]+nums[(i-1)//2+1])
        return max(nums)