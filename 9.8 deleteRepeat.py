# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3


解法——两步走：
第一步【起始行：while l1 and prev.val == l1.val:】：
暂停指针prev，不断获取l1的next（下一个节点），比较其val直至删除节点到两者的val不相等为止；
第二步【起始行：if l1:】：
滑动指针prev和l1，开始新一轮的"第一步",直到l1为None后退出循环

两个提醒：
1.注意空链表的情况（即[]）；
2.在比较节点的val或滑动节点时注意节点不能为None，该种情况下需要添加is not None的条件判断。

"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 如果是空链表
        if head is None:
            return head
        # 创建需要操作的变量l1
        l1 = head
        # 维护一个指针prev
        prev = l1
        l1 = l1.next

        while l1:

            # 比较prev和l1的值是否相等，直到删除至不相等为止
            while l1 and prev.val == l1.val:
                l1 = l1.next
                prev.next = l1

            # 指针顺序滑动
            if l1:
                prev = prev.next
                l1 = l1.next

        # 返回头节点（注意不能返回l1）
        return head
    '''dic=[]
        pr=head
        if pr==None:
            return head
        dic.append(pr.val)
        while not pr.next==None:
            # print(pr.next.val)
            if pr.next.val not in dic:
                dic.append(pr.next.val)
                pr=pr.next
            else:
                pr.next=pr.next.next
        return head'''
    """class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node=head
        while node and node.next:
            if node.val==node.next.val:
                node.next=node.next.next
            else:
                node=node.next
        return head
"""