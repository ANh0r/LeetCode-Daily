class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # hashmap = {}
        # for index, num in enumerate(nums):
        #     another_num = target - num
        #     if another_num in hashmap:
        #         return [hashmap[another_num], index]
        #     hashmap[num] = index
        # return None
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []