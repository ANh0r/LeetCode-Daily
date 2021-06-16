# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        res = ListNode(-1)
        res.next = head
        pre = res
        p = head
        while p:
            if p.val == val:
                pre.next = p.next
            else:
                pre = p
            p = p.next
        return res.next
