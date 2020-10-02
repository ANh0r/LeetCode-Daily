class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # zq = 0
        # for own in S:
        #     if own in J:
        #         zq += 1
        # return zq
        # count  = 0
        # map = {}
        # for num in J:
        #     map[num] = num
        # for n in S:
        #     if map.get(n):
        #         count += 1
        # return count
        return sum(S.count(i) for i in J)


"""宝石与石头
给定宝石列表与一系列字符串
返回宝石个数"""