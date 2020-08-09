from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
       # 1,2,3,4, 5,6,7,8 index [0,4,1,5,2,6,3,7]
       nums[::2], nums[1::2] = nums[:n], nums[n:]
       return nums

    # result = []
    # for i in range(int(len(nums) / 2)):
    #     result.append(nums[i])
    #     result.append(nums[i + n])
    # return result
t = Solution()
print(t.shuffle([1,2,3,4,5,6],3))