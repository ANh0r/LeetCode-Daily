# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        a = []
        cur = head
        while (cur):
            a.append(cur.val)
            cur = cur.next
        if left>1:
            a = a[:left-1] + a[right-1:left-2:-1] + a[right:]
        else:
            a = a[right-1::-1] + a[right:]
        cur = head
        i = 0
        while (cur):
            cur.val = a[i]
            cur = cur.next
            i += 1
        return head