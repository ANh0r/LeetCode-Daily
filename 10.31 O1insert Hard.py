class RandomizedCollection:

    def __init__(self):
        self.vals=[]
        self.index={}
    def insert(self, val: int) -> bool:
        self.vals.append(val)
        if val in self.index:
            self.index[val].add(len(self.vals)-1)
            return False
        else:
            self.index[val] = {len(self.vals)-1}
            return True
    def remove(self,val):
        if val not in self.index:
            return False
        last = len(self.vals)-1
        idx = self.index[val].pop()
        if len(self.index[val])==0:
            del self.index[val]
        if idx!=last:
            self.vals[idx] = self.vals[last]
            self.index[self.vals[idx]].remove(last)
            self.index[self.vals[idx]].add(idx)
        self.vals.pop()
        return True
    def getRandom(self) -> int:
        if self.vals:
            return self.vals[random.randint(0,len(self.vals)-1)]



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

"""设计一个支持在平均 时间复杂度 O(1) 下， 执行以下操作的数据结构。

注意: 允许出现重复元素。

insert(val)：向集合中插入元素 val。
remove(val)：当 val 存在时，从集合中移除一个 val。
getRandom：从现有集合中随机获取一个元素。每个元素被返回的概率应该与其在集合中的数量呈线性相关。
示例:

// 初始化一个空的集合。
RandomizedCollection collection = new RandomizedCollection();

// 向集合中插入 1 。返回 true 表示集合不包含 1 。
collection.insert(1);

// 向集合中插入另一个 1 。返回 false 表示集合包含 1 。集合现在包含 [1,1] 。
collection.insert(1);

// 向集合中插入 2 ，返回 true 。集合现在包含 [1,1,2] 。
collection.insert(2);

// getRandom 应当有 2/3 的概率返回 1 ，1/3 的概率返回 2 。
collection.getRandom();

// 从集合中删除 1 ，返回 true 。集合现在包含 [1,2] 。
collection.remove(1);

// getRandom 应有相同概率返回 1 和 2 。
collection.getRandom();
"""