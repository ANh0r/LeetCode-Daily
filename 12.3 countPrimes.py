class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        else:
            # 首先生成了一个全部为1的列表
            output = [1] * n
            # 因为0和1不是质数,所以列表的前两个位置赋值为0
            output[0],output[1] = 0,0
             # 此时从index = 2开始遍历,output[2]==1,即表明第一个质数为2,然后将2的倍数对应的索引
             # 全部赋值为0. 此时output[3] == 1,即表明下一个质数为3,同样划去3的倍数.以此类推.
            for i in range(2,int(n**0.5)+1):
                if output[i] == 1:
                    output[i*i:n:i] = [0] * len(output[i*i:n:i])
         # 最后output中的数字1表明该位置上的索引数为质数,然后求和即可.
        return sum(output)
"""
这题搜到一个非常牛逼的算法,叫做厄拉多塞筛法. 比如说求20以内质数的个数,首先0,1不是质数.2是第一个质数
然后把20以内所有2的倍数划去.2后面紧跟的数即为下一个质数3,然后把3所有的倍数划去.3后面紧跟的数即为下一个质数5
再把5所有的倍数划去.以此类推.

代码的实现上用了非常好的技巧
"""