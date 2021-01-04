class Solution:
    def fib(self, N: int) -> int:
        # A = [0, 1]
        # for i in range(N - 1):
        #  end(A[-1] + A[-2])
        # return A[N]
        # #递归
        return int((5**0.5)*0.2*( ((1+5**0.5)/2)**N-((1-5**0.5)/2)**N))