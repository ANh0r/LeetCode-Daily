# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_h = self.minDepth(root.left)
        right_h = self.minDepth(root.right)
        if left_h and right_h:
            return min(left_h,right_h) + 1
        if not left_h and right_h:
            return right_h + 1
        if left_h and not right_h:
            return left_h + 1
        if not left_h and not right_h:
            return 1


'''
def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        min_depth = 10**9
        if root.right:
            min_depth = min(self.minDepth(root.right),min_depth)
        if root.left:
            min_depth = min(self.minDepth(root.left),min_depth)
        return min_depth+1'''
'''class Solution:
    class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return 0
            else:
                if root and root.left and root.right:
                    return min(helper(root.left) + 1, helper(root.right) + 1)
                elif root and root.left and not root.right:
                    return helper(root.left) + 1
                elif root and not root.left and root.right:
                    return helper(root.right) + 1
                elif root and not root.left and not root.right:
                    return 1
                else:
                    return 0
        return helper(root)'''