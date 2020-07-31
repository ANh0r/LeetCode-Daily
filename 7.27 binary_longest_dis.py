class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        strs = bin(N)[2:]
        i = strs.index('1')
        j = len(strs)
        # i,j = (s := bin(N)[2:]).index('1'), len(s)
        while i <= j:
            if strs[j - 1] == '1':
                break
            else:
                j -= 1
        s = strs[i:j]
        # 计算剩余字符串内最大连续0的个数
        key = max([len(i) for i in s.split('1')]) + 1 if len(s) > 1 else 0
        return key
