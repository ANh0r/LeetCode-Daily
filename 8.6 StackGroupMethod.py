from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        # normal_list = [i for i in grp]
        for i in range(1,n+1):
            if i not in target:
                if i > target[-1]:
                    break
                res.append("Push")
                res.append("Pop")
            else:
                res.append("Push")
        return res
# [1,2,3,4,5]
# [2,3,6]


t = Solution()
print(t.buildArray([1,2,3,5],4))


#  有一说一，我觉得这个题可能用C或者Java更简单一点