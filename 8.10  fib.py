def fib(self, N: int) -> int:
    A = [0, 1]
    for i in range(N - 1):
        end(A[-1] + A[-2])
    return A[N]
'''
    if N < 2:
            return N
        return self.fib(N - 1) + self.fib(N - 2)'''
    # 递归


'''
/ 递推 O(n)
func fib2(N int) int {
    nMap := make(map[int]int)
    nMap[0] = 0
    nMap[1] = 1
    
    for i := 2; i <= N; i++ {
        nMap[i] = nMap[i-1] + nMap[i-2]
    }
    
    return nMap[N]
    }
    
    // 通项公式 O(n),主要复杂在Pow的解法上
    func fib3(N int) int {
    sr := math.Sqrt(5)
    fn := 1 / sr * (math.Pow((1+sr)/2, float64(N)) - math.Pow((1-sr)/2, float64(N)))
    return int(fn)
}
'''