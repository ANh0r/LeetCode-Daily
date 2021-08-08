class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * n
        dp[0] = 1
        ptrs = {}
        vals = {}
        for prime in primes:
            ptrs[prime] = 0
        for i in range(1, n):
            for prime in primes:
                val = dp[ptrs[prime]] * prime
                vals[prime] = val
            dp[i] = min(vals.values())
            for prime in primes:
                if dp[i] == vals[prime]:
                    ptrs[prime] += 1
        return dp[n - 1]