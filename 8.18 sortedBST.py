# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return
        return self.dfs(head,None)

    def dfs(self,start,end):
        fast = slow = start
        if start == end:
            return
        while fast != end and fast.next != end:
            slow = slow.next
            print(slow)
            fast = fast.next.next
            print(fast)
        root = TreeNode(slow.val)
        print(root)
        root.left = self.dfs(start,slow)
        root.right = self.dfs(slow.next,end)
        return root
    '''def getMedian(left: ListNode, right: ListNode) -> ListNode:
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def buildTree(left: ListNode, right: ListNode) -> TreeNode:
            if left == right:
                return None
            mid = getMedian(left, right)
            root = TreeNode(mid.val)
            root.left = buildTree(left, mid)
            root.right = buildTree(mid.next, right)
            return root
        
        return buildTree(head, None)

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/solution/you-xu-lian-biao-zhuan-huan-er-cha-sou-suo-shu-1-3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def mapListToValues(self, head):
#         vals = []
#         while head:
#             vals.append(head.val)
#             head = head.next
#         return vals

#     def sortedListToBST(self, head: ListNode) -> TreeNode:
#         values = self.mapListToValues(head)
#         def convertListToBST(left, right):
#             if left > right: return None 
#             mid = (left + right) // 2
#             node = TreeNode(values[mid])          
#             node.left = convertListToBST(left, mid-1)
#             node.right = convertListToBST(mid+1, right)
#             return node
#         return convertListToBST(0, len(values)-1) 


class Solution:
    def mapListToValues(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals    
    def sortedListToBST(self, head):
        values = self.mapListToValues(head)
        def convertListToBST(l, r):
            if l > r: return None
            mid = (l + r) // 2
            node = TreeNode(values[mid])
            if l == r:
                return node
            node.left = convertListToBST(l, mid - 1)
            node.right = convertListToBST(mid + 1, r)
            return node
        return convertListToBST(0, len(values) - 1)
        
        '''