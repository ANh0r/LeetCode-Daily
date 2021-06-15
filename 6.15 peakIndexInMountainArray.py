class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        ans = -1

        for i in range(1, n - 1):
            if arr[i] > arr[i + 1]:
                ans = i
                break

        return ans