class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            for j in range((len(A) + 1) // 2):
                if A[i][j] == A[i][-1 - j]:
                    t = 1 - A[i][j]
                    A[i][j] = A[i][-1 - j] = t

        return A