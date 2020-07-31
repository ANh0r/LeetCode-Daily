class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        res = '1'
        for i in range(2, n+1):
           # print('n = ' + str(n))
            ans = ''
            j = 0
            while j < len(res):
                k = j
                print('k = ' + str(k))
                print('j = ' + str(j))
                while k < len(res)-1 and res[k] == res[k+1]:
                    k+=1
                    print('k\' = ' + str(k))
                    print('j\' = ' + str(j))
                print('res = ' + res)
                ans += str(k+1-j)+res[k]
                print('ans = ' + ans)
                j = k+1
            res = ans
        return res


t = Solution()
print(t.countAndSay(3))

