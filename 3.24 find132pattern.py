class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        _MIN = float('-inf')

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < _MIN:
                return True
            while stack and nums[i] > stack[-1]:
                _MIN = stack.pop()
            stack.append(nums[i])

        return False