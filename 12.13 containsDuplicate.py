class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 异或方法是找到重复数字，此题用set可以解决
        # 用hash
        hashmap = {}
        for i in nums:
            if i in hashmap:
                return True
            else:
                hashmap[i] = 1
        return False