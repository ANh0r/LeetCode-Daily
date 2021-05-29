class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def subarraySum(nums: List[int], k: int) -> int:
            mp = Counter([0])
            count = pre = 0
            for x in nums:
                pre += x
                if pre - k in mp:
                    count += mp[pre - k]
                mp[pre] += 1
            return count

        m, n = len(matrix), len(matrix[0])
        ans = 0
        # 枚举上边界
        for i in range(m):
            total = [0] * n
            # 枚举下边界
            for j in range(i, m):
                for c in range(n):
                    # 更新每列的元素和
                    total[c] += matrix[j][c]
                ans += subarraySum(total, target)

        return ans