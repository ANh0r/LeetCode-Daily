
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        N = len(arr)
        up = [1] * N
        down = [1] * N
        res = 1
        for i in range(1, N):
            if arr[i - 1] < arr[i]:
                up[i] = down[i - 1] + 1
                down[i] = 1
            elif arr[i - 1] > arr[i]:
                up[i] = 1
                down[i] = up[i - 1] + 1
            else:
                up[i] = 1
                down[i] = 1
            res = max(res, max(up[i], down[i]))
        return res