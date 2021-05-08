class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        if k == len(jobs):
            return max(jobs)

        def dfs(num, groups, target):
            if not num:
                return True
            v = num.pop()
            # print(groups)
            for i, group in enumerate(groups):
                # print(i,num,v)
                if group + v <= target:
                    groups[i] += v
                    if dfs(num, groups, target): return True
                    groups[i] -= v
                if not group:  # 剪枝按照顺序分配
                    # print(group)
                    break
            num.append(v)
            return False

        jobs.sort()
        i, j = jobs[-1], sum(jobs)
        while i < j:
            mid = i + (j - i) // 2
            # print(i,j,mid)
            if dfs(jobs[:], [0] * k, mid):
                j = mid
            else:
                i = mid + 1
        return i