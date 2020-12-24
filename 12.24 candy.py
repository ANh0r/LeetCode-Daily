class Solution:
    def candy(self, ratings: List[int]) -> int:
        s = 0
        n = len(ratings)
        s += n
        tmp = [0] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                tmp[i] = tmp[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                tmp[i] = max(tmp[i], tmp[i + 1] + 1)
        s += sum(tmp)
        return s


"""先给每个人一个糖，初始化tmp数组为额外糖果。从左向右遍历，如果i+1分数高，tmp[i+1]=tmp[i]+1。再从后往前遍历，
如果i比i+1分数高，那么比较tmp[i]和tmp[i+1]+1，如果tmp[i]小，更新。假如分数i-1<i，那么下一次继续检查，如果分数i-1>i，
因为第一次tmp[i]>tmp[i-1]，从右往左更新tmp[i]只可能增加，依然满足大小关系
"""