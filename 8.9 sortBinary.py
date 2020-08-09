from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr,key=lambda x:(bin(x).count('1'),x))


print(Solution().sortByBits([7,6,5,8,9]))



