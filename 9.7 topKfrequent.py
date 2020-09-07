class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return [i for i, _ in Counter(nums).most_common(k)] 黑魔法
        def heap(i, k):  # 维护小顶堆
            while True:
                child = 2 * i + 1  # t为节点孩子的index
                if child >= k:
                    return
                if child + 1 < k and hashlist[child][1] > hashlist[child + 1][1]:
                    child = child + 1
                if hashlist[child][1] < hashlist[i][1]:
                    hashlist[child], hashlist[i] = hashlist[i], hashlist[child]
                    i = child
                else:
                    return

        # 建立hash表
        hashmap = dict()
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        # 将hashmap转换为二维list
        hashlist = [[key, value] for key, value in hashmap.items()]
        # 建立k个元素的最小堆
        for i in range(k // 2, -1, -1):  # 从底部建立堆 将最小的元素放在堆顶
            heap(i, k)
        # 剩余依次和堆顶比较
        for i in range(k, len(hashlist)):
            if hashlist[i][1] > hashlist[0][1]:
                hashlist[0] = hashlist[i]
                heap(0, k)
        return [hashlist[i][0] for i in range(k)]


"""返回数组中频次前k的元素
思路：hash+堆排序
"""