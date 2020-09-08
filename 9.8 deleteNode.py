"""请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为 要被删除的节点 。

示例 1：

输入：head = [4,5,1,9], node = 5
输出：[4,1,9]
解释：给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2：

输入：head = [4,5,1,9], node = 1
输出：[4,5,9]
解释：给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
"""
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        '''只给定被删除的节点，删除该节点，给定的不是链表/head'''
        # method: 找到该节点， 直接将该节点变为该节点的下一个节点
        node.val = node.next.val
        node.next = node.next.next
        # 就是跳过一下给定的节点，问题在与如果实例给的是重复的，比如[1,2,2,3,5]中删除了2节点
        # 题意应该是两个节点都能删除

