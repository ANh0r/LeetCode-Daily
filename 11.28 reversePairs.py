class Solution:
    def find_reversed_pairs(self, nums, left, right):
        res, mid = 0, (left + right) // 2

        j = mid + 1
        for i in range(left, mid + 1):
            while j <= right and nums[i] > 2 * nums[j]:
                res += mid - i + 1
                j += 1
        return res

    def merge_sort(self, nums, nums_sorted, l, r):
        if l >= r: return 0
        mid = (l + r) // 2
        res = self.merge_sort(nums, nums_sorted, l, mid) + \
              self.merge_sort(nums, nums_sorted, mid + 1, r) + \
              self.find_reversed_pairs(nums, l, r)

        i, j, k = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                nums_sorted[k] = nums[i]
                i += 1
            else:
                nums_sorted[k] = nums[j]
                j += 1
            k += 1

        while i <= mid:
            nums_sorted[k] = nums[i]
            i += 1
            k += 1
        while j <= r:
            nums_sorted[k] = nums[j]
            j += 1
            k += 1

        for k in range(l, r + 1): nums[k] = nums_sorted[k]

        return res

    def reversePairs(self, nums: List[int]) -> int:
        if not nums: return 0
        nums_sorted = [0] * len(nums)
        return self.merge_sort(nums, nums_sorted, 0, len(nums) - 1)
"""
        给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。

你需要返回给定数组中的重要翻转对的数量。

示例 1:

输入: [1,3,2,3,1]
输出: 2
示例 2:

输入: [2,4,3,5,1]
输出: 3
"""