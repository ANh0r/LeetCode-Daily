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

        
'''class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        left_min = self.minDepth(root.left)
        right_min = self.minDepth(root.right)
        if not root.left or not root.right:
            return left_min+1 if root.left else right_min +1
        if not root.left and not root.right:
            return 1
        return min(left_min,right_min) +1'''