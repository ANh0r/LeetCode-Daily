# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # if not head or not head.next:
        #     return head
        # newh = head.next
        # head.next = self.swapPairs(newh.next)
        # newh.next = head
        # return newh
        if not head or not head.next:
            return head
        tmp = self.swapPairs(head.next.next)# 这部分可以继续走下去，用方法中的凉凉交换继续交换，完成后返回给head.next
        res = head.next
        res.next = head
        head.next = tmp
        return res


"""
交换链表中相邻的节点
思路：
递归）
'''用 head 表示原始链表的头节点，新的链表的第二个节点，
        用 newHead 表示新的链表的头节点，原始链表的第二个节点，则原始链表中的其余节点的头节点是 newHead.next。
        令 head.next = swapPairs(newHead.next)，表示将其余节点进行两两交换，交换后的新的头节点为 head 的下一个节点。
        然后令 newHead.next = head，即完成了所有节点的交换。最后返回新的链表的头节点 newHead
         ![](https://pictures.ryanhor.com/20201013083930.png) '''
1.递归终止条件：节点的next为空，或者只剩下一个元素
2.返回值：上次交换完成的子链表
3.因为递归是重复做一样的事情，所以从宏观上考虑，只用考虑某一步是怎么完成的。我们假设待交换的俩节点分别为head和next，
next的应该接受上一级返回的子链表(参考第2步)。就相当于是一个含三个节点的链表交换前两个节点，就很简单了，想不明白的画画图就ok

"""