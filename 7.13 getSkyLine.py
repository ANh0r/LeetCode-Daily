class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 把左边界和右边界的坐标保留下来
        x = [i[0] for i in buildings] + [i[1] for i in buildings]
        # 排序
        x.sort()
        index = 0
        heap = []
        res = [[0, 0]]
        # 从小到大的顺序循环边界的值
        for i in x:
            # index表示的是建筑的编号，找到建筑左边界等于i的建筑放到大根堆
            while index < len(buildings) and buildings[index][0] == i:
                # 大根堆存放的是（高，右边界）
                heapq.heappush(heap, (-buildings[index][2], buildings[index][1]))
                # 建筑编号加1
                index += 1

            # 大根堆的堆顶元素即建筑的最高值，如果这栋建筑的右边界小于等于i，即该建筑已经遍历完了，不需要了，则从堆中移出
            while heap and heap[0][1] <= i:
                heapq.heappop(heap)
            # 如果堆里有值，把堆顶的元素的高取出来
            h = -heap[0][0] if heap else 0
            # 和结果中的高进行对比，如果不相同，说明不在一条直线上，把该值添加到res中
            if h != res[-1][1]:
                res.append([i, h])

        return res[1:]