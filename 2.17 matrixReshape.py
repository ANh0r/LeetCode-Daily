class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        # if len(nums)*len(nums[0])!=r*c:
        #     return nums
        # l=[]
        # new=[]
        # for i in range(len(nums)):
        #     l+=nums[i]
        # for i in range(0,len(l),c):
        #     new.append(l[i:i+c])
        # return new
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums

        ans = [[0] * c for _ in range(r)]
        for x in range(m * n):
            ans[x // c][x % c] = nums[x // n][x % n]

        return ans