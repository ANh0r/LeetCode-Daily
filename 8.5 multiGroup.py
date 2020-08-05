class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = 0
        count = 0

        for n in nums:
            if count == 0:
                major = n
            if n == major:
                count = count + 1
            else:
                count = count - 1

        return major
#  摩尔投票法：在众数大于n/2时有奇效，但缺点在于仅能在多数唯一且存在，且频数大于n/2时可用