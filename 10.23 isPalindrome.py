# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        """
        快慢指针找两部分的起始点
        :param head:
        :return: 慢指针节点
        """
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        """
        1.先确定当前节点current，并说明下一节点next.node = current.next
        2.因为是重复操作，所以链表需要先指向下一节点，current.next = previous ，再更改本身
        3.更改本身 previous = current
        4.移动链表 current = next.node 注意此处不用current.next是因为此时current.next实际上是previous，即我们刚才已经遍历的。
        5.下一次循环时候：
        a. next.node = 第三个节点
        b. 当前节点的后一个节点是上一步的current
        c. 当前节点的下一个节点指向本节点，先不更改
        d. 下一次循环更改指向
        6。 最后一次循环时，即current = next_node这里next.node不为空的最后一个条件：
        a. next_node = current.next -> current.next = None
        b. current.next = previous -> previous = 上一步的head
        c. previous = current -> 本节点
        d. current = next_node -> next_node = None 跳出循环，此时返回previous即本节点，而且也指向了正常节点

        :param head:
        :return: 翻转链表的头结点
        """
        previous = None
        current = head
        while current is not None:
            next_node = current.next

            current.next = previous
            previous = current
            current = next_node
        return previous