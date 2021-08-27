from heapq import *


class MedianFinder:

    def __init__(self):
        self.max_h = []
        self.min_h = []
        heapify(self.max_h)
        heapify(self.min_h)

    def addNum(self, num: int) -> None:
        if not self.max_h:
            heappush(self.max_h, -num)
            return
        if not self.min_h:
            tmp = -heappop(self.max_h)
            if num >= tmp:
                heappush(self.max_h, -tmp)
                heappush(self.min_h, num)
            else:
                heappush(self.max_h, -num)
                heappush(self.min_h, tmp)
        else:
            if num < -self.max_h[0]:
                if len(self.max_h) <= len(self.min_h):
                    heappush(self.max_h, -num)
                else:
                    tmp = -heappop(self.max_h)
                    heappush(self.min_h, tmp)
                    heappush(self.max_h, -num)
            elif -self.max_h[0] <= num <= self.min_h[0]:
                if len(self.max_h) < len(self.min_h):
                    heappush(self.max_h, -num)
                else:
                    heappush(self.min_h, num)
            else:
                if len(self.max_h) >= len(self.min_h):
                    heappush(self.min_h, num)
                else:
                    tmp = heappop(self.min_h)
                    heappush(self.max_h, -tmp)
                    heappush(self.min_h, num)

    def findMedian(self) -> float:
        # print(self.max_h,"====",self.min_h)
        max_len = len(self.max_h)
        min_len = len(self.min_h)

        if min_len == max_len:
            return (-self.max_h[0] + self.min_h[0]) / 2.
        elif max_len > min_len:
            return -self.max_h[0] * 1.
        else:
            return self.min_h[0] * 1.


"""
from heapq import *
class MedianFinder:
    def __init__(self):
        self.max_h = []
        self.min_h = []
        heapify(self.max_h)
        heapify(self.min_h)

    def addNum(self, num):
       # 每次都插入到最小堆，然后，将最小堆里面的栈顶元素，
       # 取出来，放到最大堆中去，这样就能保证最小堆的堆，都比最大堆的堆顶大
       #（因为最大堆是最小堆，一泡屎一趴尿，拉扯大的。）
       # 下面的调整，使得最小最大堆元素相差最多为1，而且永远是 最小堆元素个数大于  等于最大堆元素个数
        heappush(self.min_h,num)
        heappush(self.max_h,-heappop(self.min_h))
        if len(self.min_h) < len(self.max_h):
            heappush(self.min_h,-heappop(self.max_h))

    def findMedian(self):
        max_len = len(self.max_h)
        min_len = len(self.min_h)
        return self.min_h[0]*1. if max_len!=min_len else (-self.max_h[0]+self.min_h[0])/2.
"""