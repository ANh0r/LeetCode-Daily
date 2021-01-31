class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n=len(strs)
        parent=list(range(n))
        size=[1]*n
        nSet=n

        def find(a):
            if parent[a]!=a:
                parent[a]=find(parent[a])
            return parent[a]

        def union(a,b):
            a,b=find(a),find(b)
            if a==b: return False
            if size[a]<size[b]:
                a,b=b,a
            parent[b]=a
            size[a]+=size[b]
            nonlocal nSet
            nSet-=1
            return True

        l=len(strs[0])
        for i in range(n-1):
            for j in range(i+1,n):
                diff=None
                for k in range(l):
                    c1,c2=strs[i][k],strs[j][k]
                    if c1!=c2:
                        if diff is None:
                            diff=(c1,c2)
                        elif diff==(c2,c1):
                            diff=0
                        else: break
                else:
                    union(i,j)
        return nSet