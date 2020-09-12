"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        n = len(candidates)
        res = []
        candidates.sort()

        def helper(i, tmp, target):
            if (target == 0):
                res.append(tmp)
                return
            if (i == n or target < candidates[i]):
                return
            helper(i, tmp + [candidates[i]], target - candidates[i])
            helper(i + 1, tmp, target)

        helper(0, [], target)
        return res
'''
candidates.sort()
n = len(candidates)
res = []

def helper(i, tmp_sum, tmp):
    if tmp_sum > target or i == n:
        return
    if tmp_sum == target:
        res.append(tmp)
        return
    helper(i, tmp_sum + candidates[i], tmp + [candidates[i]])
    helper(i + 1, tmp_sum, tmp)

helper(0, 0, [])
return res
'''
'''
def dfs(result,path,cand,cur_target,cur_index):
            path = path.copy()
            if cur_target == 0:
                result.append(path)
                return 
            if cur_index > len(cand) - 1:
                return
            for index in range(cur_index,len(cand)):
                temp = cur_target - cand[index]
                if temp < 0:
                    return    
                path.append(cand[index])
                dfs(result,path,cand,temp,index)
                path.pop()

        if len(candidates) == 0:
            return []
        res = []
        path = []
        candidates.sort()
        dfs(res,path,candidates,target,0)
        return res
        '''