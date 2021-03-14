class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = [[] for _ in range(20011)]  # 开辟一个大数组，长度为质数，注意这里不能用 [[]] * 20011
        # 一般定义成离2的整次幂比较远的质数，这样取模之后冲突的概率比较低。

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        t = key % 20011
        for item in self.hash[t]:  # 遍历哈希到的链表中，查找key,并更新值
            if item[0] == key:
                item[1] = value
                return  # 更新完之后，直接返回
        self.hash[t].append([key, value])  # 如果链表中找不到对应的key，将其新添到链表中

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        t = key % 20011
        for item in self.hash[t]:
            if item[0] == key:
                return item[1]
        return -1  # 可能哈希的位置，所对应的链表不为空，但是不存在该值

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        t = key % 20011
        delete = []
        for item in self.hash[t]:
            if item[0] == key:
                delete = item  # remove方法，这里可以偷懒，把对应的value值设为-1，即表示它已经删除
        if delete:
            self.hash[t].remove(delete)

"""作者：jho9o5
链接：https://leetcode-cn.com/problems/design-hashmap/solution/python3-xiang-xi-ti-jie-la-lian-fa-shi-xian-by-jho/"""