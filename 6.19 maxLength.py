class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.res = 0
        self.dfs(0, arr, '')
        return self.res
    def dfs(self,index, arr, tmp):
        if len(set(tmp)) == len(tmp):
            self.res = max(self.res, len(tmp))
        for i in range(index, len(arr)):
            self.dfs(i+1, arr, tmp + arr[i])