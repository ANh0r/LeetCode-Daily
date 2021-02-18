class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        res,cur = 0,0
        for i in range(0,len(A)):
            if  i >= K and A[i-K] == 2:
                cur -= 1
            if cur%2 == A[i]:
                if (i+K>len(A)):
                    return -1
                A[i] = 2
                res += 1
                cur += 1
        return res