class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k  = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k +=1
        return k
"""
n = len(nums)
        if n == 0:
            return 0
        slow = 0
        fast = 0
        while fast<n:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1 #这里不能加else，因为快指针是一定要一直往前去的，慢指针加一的条件是快指针的元素加进来
        return slow
"""