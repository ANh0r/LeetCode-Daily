class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n, total, sl, ans = len(nums1), 0, sorted(nums1), inf
        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            total += diff
            if diff + ans <= 0: continue  # mark
            idx = bisect.bisect_left(sl, nums2[i])
            if idx:
                ans = min(ans, abs(sl[idx-1] - nums2[i]) - diff)
            if idx < n:
                ans = min(ans, abs(sl[idx] - nums2[i]) - diff)
        return (total + ans) % (10 ** 9 + 7) if total else total