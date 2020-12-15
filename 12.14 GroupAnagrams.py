from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = dict()
        # for item in strs:
        #     key = tuple(sorted(item)) # 关键是排序后的字符都要相等
        #     # sorted函数返回字符列表, 必须转换为tuple才能作为字典的键值
        #     if key in res:
        #         res[key] += [item]
        #     else:
        #         res[key] = [item]
        # return list(res.values())

        # 遍历寻找不同排列，如果相同则做上标记
        # n = len(strs)
        # visited = [False] * n
        # res = []
        # for i in range(n):
        #     if visited[i]:
        #         continue
        #     base = [0] * 26
        #     tmp = [strs[i]]
        #     for char in strs[i]:
        #         base[ord(char)-ord('a')] += 1
        #     j = i + 1
        #     while j < n:
        #         if not visited[j]:
        #             count = [0] * 26
        #             for char in strs[j]:
        #                 count[ord(char)-ord('a')] += 1
        #             if count == base:
        #                 tmp.append(strs[j])
        #                 visited[j] = True
        #         j += 1
        #     res.append(tmp)
        # return res

        res = {}
        for i in strs:
            key = tuple(sorted(i))
            if key in res:
                res[key].append(i)
            else:
                res[key] = [i]
        return list(res.values())