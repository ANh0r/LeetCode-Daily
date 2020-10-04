# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = ListNode() # 保留完整的链表
        l3 = a  # 保留完整的链表
        c = 0  # 进位
        while l1 or l2:
            x=l1.val if l1 else 0  # 没有下一节点时取0
            y=l2.val if l2 else 0
            tmp = x+y
            if tmp+c <10:
                l3.next = ListNode(tmp+c)
                c=0  # 不进位，清零
            else:
                l3.next = ListNode(tmp+c-10)
                c=1  # 进位，进1
            # print(tmp)
            # print(l1)
            # print(l2)
            if l1:
                l1 = l1.next  # 进入链表的下一节点
            if l2:
                l2 = l2.next  # 进入链表的下一节点
            l3 = l3.next
        if c==1:
            l3.next = ListNode(1)  # 最后一个进位增加一个末尾节点，元素为1
        return a.next  # a的第一个是0，因此去头节点
    '''dummy=p=ListNode(None)
        s=0
        while l1 or l2 or s:
            s+=(l1.val if l1 else 0)+(l2.val if l2 else 0)
            p.next=ListNode(s%10);
            p=p.next
            s//=10
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next'''


"""

链表由节点传成，每个节点分为数据域和指针域，数据域存放元素，指针域存放下一个节点的地址。
python没有指针，所有变量都是对象，因此只能模拟一个链表。
模拟的val就是节点数据，next就是下一个节点。

"""