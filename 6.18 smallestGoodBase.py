class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)

        def check(x, m):
            ans = 0
            for _ in range(m + 1):
                ans = ans * x + 1
            return ans

        ans = float("inf")
        for i in range(1, 64):
            l = 2
            r = num
            while l < r:
                mid = l + (r - l) // 2
                tmp = check(mid, i)
                if tmp == num:
                    ans = min(ans, mid)
                    break
                elif tmp < num:
                    l = mid + 1
                else:
                    r = mid

        return str(ans)