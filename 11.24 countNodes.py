# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        # retu
        return left+right+1
    """
    完全二叉树的节点个数
    直接一个递归，类似于斐波那契一样的递归
1.你先求左边子树是，一直向下走，当你递到比如示例节点4那里，接着向下递，4不为空，向下，他的左边为空，下去，返回一个return 0；
同样，他的右边下去还是返回一个0，接着这次向下，return left+right+1(1是4这个根节点)，返回的是1；
2.那么就这样一次一次的在递归回去，就得到节点数目了。

    """