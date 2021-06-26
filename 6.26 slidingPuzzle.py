class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """
        :type board: List[List[int]]
        :rtype: int
        """
        row = len(board)
        col = len(board[0])
        er_one = [None] * (row * col)
        # 二维转换一维
        for i in range(row):
            for j in range(col):
                er_one[i * col + j] = board[i][j]
        # 最后跳出循环的条件
        c_loc = [0]*(row*col)
        for i in range(1,row*col):
            c_loc[i-1] = i
        # 步数
        step = 0
        # 方向
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        # 当前情况
        cur = [er_one]
        # 已访问的情况
        visited = set()
        while cur:
            next_time = []
            for tmp in cur:
                # 当此时的情况和正确的情况一样是,返回步数
                if tmp == c_loc:
                    return step
                # 没有访问过的情况
                if tuple(tmp) not in visited:
                    # 添加到已访问
                    visited.add(tuple(tmp))
                    # 找到一维数组的0的位置
                    zero_loc = tmp.index(0)
                    # 找到对应二维数组的行和列
                    x, y = divmod(zero_loc, col)
                    # 进行上下左右交换
                    for p,q in dirs:
                        tmp_x = x + p
                        tmp_y = y + q
                        if  0<=tmp_x < row and 0<=tmp_y<col:
                            # 要拷贝一份
                            tmp_tmp = tmp[:]
                            tmp_tmp[tmp_x*col+tmp_y],tmp_tmp[zero_loc] = tmp_tmp[zero_loc],tmp_tmp[tmp_x*col+tmp_y]
                            next_time.append(tmp_tmp)
            step += 1
            cur = next_time
        return -1
"""
首先,分析这题,这道题是2X3的,为了让它更有一般性,我准备做nXm,也就是可以适应任何情况.有一个空白处,就是我们可以和它的上下左右交换,题中要我们找出最少步数,所以毫不犹豫用BFS;

其次,用BFS有几个难点,1. 我们需要达到什么样情况,就说明已经完成,找出最后跳出条件;2. 因为board是二维数组,对计算机不是很友好,如果能转化成一维的数组,那就好了;3.要记录已经访问过的情况,不能重复访问,造成死循环.

接下来,我们解决上面问题,第一个问题,本题中只要找出[[1,2,3],[4,5,0]],所以我们找出更有一般性的条件;第二个问题,二维数组转换一维数组,用borad[i][j] -> er_one[i*col+j],可以一一对应;第三问题,我们记录已访问的情况,就可以了.

最后,我们一起看代码,我用注释解释各个地方用处
"""