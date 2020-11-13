# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
       if head == None: return head
       point1, point2 = head, head.next
       p1, p2 = point1, point2
       while p2 != None and p2.next:
           p1.next = p1.next.next
           p2.next = p2.next.next
           p1 = p1.next
           p2 = p2.next
       p1.next = point2
       return point1