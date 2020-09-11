"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]


"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n < 1:
            return []
        nums = [i for i in range(1, 10)]

        def dfs(start_index, nums, path, n, k, res, depth):
            if n == 0 and depth == k:
                res.append(path[:])
                return
            for i in range(start_index, len(nums)):
                if nums[i] <= n:
                    path.append(nums[i])
                    dfs(i + 1, nums, path, n - nums[i], k, res, depth + 1)
                    path.pop()

        start_index = 0
        path = []
        res = []
        depth = 0
        dfs(start_index, nums, path, n, k, res, depth)
        return res

    '''
    class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def Search(number, oneSum, oneSolution):
            if oneSum == 0 and len(oneSolution) == k:  # 找到了正确的解
                totalSolutions.append(oneSolution[:])  # 注意要切片一下。相当于复制了一遍内容。
                return

            if number == 10:  # 1~9查完了
                return

            if oneSum < 0:  # 数组和大于n了
                return

            if len(oneSolution) > k:  # 数组长度大于k了
                return

            Search(number + 1, oneSum - number, oneSolution + [number])  # 选了这个数
            Search(number + 1, oneSum, oneSolution)   # 没选择这个数

        totalSolutions = []

        Search(1, n, [])

        return totalSolutions
    '''