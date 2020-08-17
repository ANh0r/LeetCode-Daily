import collections


class RecentCounter(object):
    def __init__(self):
        self.q = collections.deque()

    def ping(self, t):
        self.q.append(t)
        while self.q[0] < t-3000:
            self.q.popleft()
        return len(self.q)
'''
def __init__(self):
        self.queue = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)
        while (len(self.queue) != 0) and (self.queue[0] < t - 3000):
            self.queue.pop(0)
        return len(self.queue)
        '''

'''一道没看懂的题：
写一个 RecentCounter 类来计算最近的请求。

它只有一个方法：ping(int t)，其中 t 代表以毫秒为单位的某个时间。

返回从 3000 毫秒前到现在的 ping 数。

任何处于 [t - 3000, t] 时间范围之内的 ping 都将会被计算在内，包括当前（指 t 时刻）的 ping。

保证每次对 ping 的调用都使用比之前更大的 t 值。

输入：inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
输出：[null,1,2,3,3]

inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]] 意思是， 在第1，100，3001，3002这四个时间点分别进行了ping请求， 在3001秒的时候， 他前面的3000秒指的是区间[1,3001]， 所以一共是有（1，100，3001）三个请求， t = 3002的前3000秒指的是区间[2, 3002], 所以有100，3001，3002三次请求。

'''