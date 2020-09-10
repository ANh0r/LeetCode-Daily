"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()
        #visited = [0]*len(candidates)

        def find(begin,tmp_list,remain,recursion):
            #print(tmp_list)
            if remain<0:
                return
            if remain==0:
                res.add(tuple(sorted(tmp_list)))
                return
            else:
                for i in range(begin,len(candidates)):
                    if candidates[i] > remain:
                        break
                    if i>begin and candidates[i]==candidates[i-1]: #i>0 and recursion==0
                        #print("continue")
                        continue

                    #if visited[i]==0:
                        #visited[i] = 1
                    tmp_list.append(candidates[i])
                    find(i+1,tmp_list,remain-candidates[i],recursion+1)
                        #visited[i] = 0


        find(0,[],target,0)
        return list(res)
"""

from typing import List


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(begin, path, residue):
            if residue == 0:
                res.append(path[:])
                return

            for index in range(begin, size):
                if candidates[index] > residue:
                    break

                if index > begin and candidates[index - 1] == candidates[index]:
                    continue

                path.append(candidates[index])
                dfs(index + 1, path, residue - candidates[index])
                path.pop()

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        res = []
        dfs(0, [], target)
        return res