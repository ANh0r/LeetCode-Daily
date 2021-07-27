# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root.left and root.right:
            left_second_max = root.left.val
            right_second_max = root.right.val
            if root.val == root.left.val:
                left_second_max = self.findSecondMinimumValue(root.left)
            if root.val == root.right.val:
                right_second_max = self.findSecondMinimumValue(root.right)

            if left_second_max == -1 or right_second_max == -1:
                return max(left_second_max, right_second_max)
            else:
                return min(left_second_max, right_second_max)

        else:
            return -1