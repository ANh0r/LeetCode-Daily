class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        t = (n+1)//2
        sum = 0

        for i in range(n):
            j = min(i+1, n-i)
            k = j//2
            s = j*(t-2*k)+(2*k+(n+1)%2)*k
            sum += arr[i]*s
        return sum