# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        :type root: TreeNode
        :rtype: bool
        """
        def height(root: TreeNode)-> int:
            if not root:
                return 0
            return max(height(root.left),height(root.right))+1
        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
# 分别做三个判断 1.当前子树是平衡的 2.左子树是平衡的 3.右子树也是平衡的 此时返回True 或者根节点为空 直接返回True
# 自顶向下

class Solution2:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.recur(root) != -1

    def recur(self, root):
        if not root: return 0
        left = self.recur(root.left)
        if left == -1: return -1
        right = self.recur(root.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1

# 自底向上，提前判断节点是否平衡


'''
def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0


'''


