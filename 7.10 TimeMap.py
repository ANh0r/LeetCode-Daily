class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dct = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dct[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        a = bisect_right(self.dct[key], [timestamp, "z"*101])
        if a-1 == len(self.dct[key]) or a == 0:
            return ""
        return (self.dct[key])[a-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)