class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        counter = {}
        res = i = diffNum = leftForward = 0

        for j in range(len(A)):

            if A[j] not in counter:
                diffNum += 1
                counter[A[j]] = 1
            else:
                counter[A[j]] +=1

            if diffNum == K:
                if A[i-1] != A[j] and i > 0:
                    leftForward = 0
                while diffNum == K:
                    if counter[A[i]] == 1:
                        diffNum -= 1
                        del counter[A[i]]
                    else:
                        counter[A[i]] -= 1
                    i += 1
                    leftForward += 1
            res += leftForward

        return res