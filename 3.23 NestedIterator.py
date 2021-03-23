# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


def gen(nestedList):
    for ele in nestedList:
        if ele.isInteger():
            yield ele.getInteger()
        else:
            yield from gen(ele.getList())


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.gen = gen(nestedList)
        self.stored = (False, 0)

    def next(self) -> int:
        if not self.hasNext():
            return -1
        result = self.stored[1]
        self.stored = (False, 0)
        return result

    def hasNext(self) -> bool:
        if self.stored[0]:
            return True
        try:
            self.stored = (True, next(self.gen))
            return True
        except:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())