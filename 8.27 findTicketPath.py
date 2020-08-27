import collections
import heapq
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(curr: str):
            while vec[curr]:
                tmp = heapq.heappop(vec[curr])
                dfs(tmp)
            stack.append(curr)
            print(curr)

        vec = collections.defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)
        for key in vec:
            heapq.heapify(vec[key])

        stack = list()
        dfs("JFK")
        return stack[::-1]





t = Solution()
t.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])

'''
1.判断0位置，如果1位置有0位置元素则可以判断该城市1位置票是0位置票的前段
List[1]->List[0]
2.重复判断，List[2]没有和前两张同样的目的地/出发点，暂时搁置
3.List[3]的0位置是List[0]的1位置，所以加入List[0]->List[3]->List[2]
4.List[1]->List[0]->List[3]->List[2]
'''