# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head
        # # 如果是空链表
        # if head is None:
        #     return head
        # # 创建需要操作的变量l1
        # l1 = head
        # # 维护一个指针prev
        # prev = l1
        # l1 = l1.next

        # while l1:

        #     # 比较prev和l1的值是否相等，直到删除至不相等为止
        #     while l1 and prev.val == l1.val:
        #         l1 = l1.next
        #         prev.next = l1

        #     # 指针顺序滑动
        #     if l1:
        #         prev = prev.next
        #         l1 = l1.next

        # # 返回头节点（注意不能返回l1）
        # return head