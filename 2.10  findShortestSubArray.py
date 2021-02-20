class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        a = {}
        for i in range(len(nums)):
            if nums[i] not in a:
                a[nums[i]] = [i]
            else:
                a[nums[i]].append(i)
        m = 0
        for i in a:
            m = max(m, len(a[i]))
        r = len(nums)
        for i in a:
            if len(a[i]) == m:
                r = min(r, a[i][-1] - a[i][0] + 1)
        return r