from typing import List

""" eleNumbers=collections.Counter(arr)
        return len(set(eleNumbers.values()))==len(eleNumbers)"""
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mapp = {}
        cnt = {}
        for i in arr:
            if i in mapp:
                mapp[i] += 1
            else:
                mapp[i] = 1
        for k in mapp.values():
            if k in cnt:
                cnt[k] += 1
                return False
            else:
                cnt[k] = 1
        return True


t = Solution()
print(t.uniqueOccurrences([1,2,2,3,1,1]))

"""
给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。

如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。

 

示例 1：

输入：arr = [1,2,2,1,1,3]
输出：true
解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。
"""