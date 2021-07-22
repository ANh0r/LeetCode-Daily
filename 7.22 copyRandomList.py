"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        p=head
        while p:
            new_node=Node(p.val,None,None)
            new_node.next=p.next
            p.next=new_node
            p=new_node.next
        p=head
        while p:
            if p.random:
                p.next.random=p.random.next
            p=p.next.next
        p=head
        dumpnode=Node(-1,None,None)
        cur=dumpnode
        while p:
            cur.next=p.next
            cur=cur.next
            p=p.next.next
        return dumpnode.next