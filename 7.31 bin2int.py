# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     def getDecimalValue(self, head: ListNode) -> int:
#         a='0b'
#         while head:
#             a += str(head.val)
#             head=head.next
#         return int(a,2)
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head is not None:
            res = res*2 + head.val
            head = head.next
            print(res)
        return int(res)


t = Solution()
head1 = ListNode(101)
print(int(t.getDecimalValue(head1)))
