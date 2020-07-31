from typing import List


class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        n, m = len(a), len(b)
        i, j, res = 0, 0, 2147483647
        while i < n and j < m:
            res = min(res, abs(a[i]-b[j]))
            if a[i] > b[j]: j += 1
            else: i += 1
        return res


t = Solution()
print(t.smallestDifference([112,24,31,24,46],[5,3,6,43,7]))



'''
Method: 1.排序
2. 判断双方第一个元素之差，如果大于0，则说明数组增大List1差值会越来越大，此时增大j，重新计算，反之增大i  ->  停止条件：某一个数组遍历结束
3.更新最小值，返回
'''