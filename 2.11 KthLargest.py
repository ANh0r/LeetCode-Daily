class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.count = k
        self.myhq = hq()#建立小根堆
        for i in range(len(nums)):
            self.myhq.push(nums[i])
        for i in range(k,len(nums)):
            self.myhq.pop()

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.myhq.push(val)
        if len(self.myhq.heap) > self.count:
            self.myhq.pop()
        return self.myhq.heap[0]

class hq(object):
    def __init__(self):
        self.heap = []

    def _shift_up(self,index):
        while index > 0:
            parent = (index-1)//2
            if self.heap[parent] < self.heap[index]:
                break

            self.heap[index],self.heap[parent] = self.heap[parent],self.heap[index]
            index = parent

    def _shift_down(self,index):
        while index*2 + 1 < len(self.heap):
            left = index*2 + 1
            right = index*2 + 2
            parent = index
            smallest = parent
            if self.heap[left] < self.heap[parent]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == parent:
                break
            self.heap[parent],self.heap[smallest] = self.heap[smallest],self.heap[parent]
            index = smallest

    def pop(self):
        last = len(self.heap) - 1
        self.heap[0],self.heap[last] = self.heap[last],self.heap[0]
        peek = self.heap.pop()
        self._shift_down(0)
        return peek

    def push(self,data):
        self.heap.append(data)
        self._shift_up(len(self.heap)-1)
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)