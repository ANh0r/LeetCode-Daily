class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for num in nums:
            a = a ^ num
        return a
    #return reduce(lambda x, y: x ^ y, nums)
    '''
    仅仅出现一次的数字可以用异或找到非重复的数字，因为相同数字异或等于0，0和一个非0数异或等于那个数字。
    异或运算满足交换律和结合律

    '''