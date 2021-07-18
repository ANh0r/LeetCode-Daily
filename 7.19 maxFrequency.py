class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        pre = [0] # 前缀和
        for num in nums:
            pre.append(pre[-1] + num)

        ans = 1
        left = 0
        for right in range(len(nums)):

            # 维护一个窗口，窗口内元素经过不超过k次操作，可全部变为最右端元素
            while nums[right] * (right - left) - (pre[right] - pre[left]) > k:
                left += 1
            ans = max(ans, right - left + 1)
        return ans