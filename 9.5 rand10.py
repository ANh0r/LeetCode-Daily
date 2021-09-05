# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            res = (rand7()-1)*7 + rand7()#构造1~49的均匀分布
            if res <= 40:#剔除大于40的值，1-40等概率出现。
                break
        return res%10+1#构造1-10的均匀分布