class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        n=len(deliciousness)
        res=0
        count=defaultdict(int)
        maxtarget=max(deliciousness)*2#需要遍历之和的最大值
        for i in range(n):
            cur=deliciousness[i]
            for j in range(22):#遍历所有幂的可能
                temp=1<<j
                if temp>=cur:
                    curtime=count.get(temp-cur,0)#用字典存放差值
                    res=(res+curtime)%(10**9+7)
                if temp>maxtarget:
                    break
            count[cur]+=1#每次自身计数要加1
        return res