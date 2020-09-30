# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        node = root
        flag = 0
        while 1:
            if val<node.val:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                node = node.right
"""
#空树，
#直接返回val节点。
#非空数，
#若小于当前节点值时，若此节点有左孩子，则节点向左推移；

若此节点无左孩子，则赋为该节点的左孩子；
#若大于等于当前节点值时，若此节点有右孩子，则节点向右推移；

若此节点无右孩子，则赋为该节点的右孩子。

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        def dfs(root,val):
            if root:
                if root.val > val:
                    if root.left:
                        dfs(root.left,val)
                    else:
                        root.left = TreeNode(val)
                if root.val < val:
                    if root.right:
                        dfs(root.right,val)
                    else:
                        root.right = TreeNode(val)
        
        dfs(root,val)
        return root

著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""