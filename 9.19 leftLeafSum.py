def sumOfLeftLeaves(self, root: TreeNode) -> int:
    self.res = 0

    def dfs(node):
        if not node:
            return None
        # 判断是否为左子节点，是否同时又是叶子节点
        if node.left and not node.left.left and not node.left.right:
            self.res += node.left.val  # 统计结果
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return self.res

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0
        stack = [root]
        while stack:
            p = stack.pop()
            if p.left and p.left.left == None and p.left.right == None:
                res += p.left.val
            if p.left: stack.append(p.left)
            if p.right: stack.append(p.right)

        return res"""
"""
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
 


著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
思路：
1.题目的要求是要找到所有的左叶子之和，那么首先先考虑什么是叶子节点。
当二叉树中一个节点既没有左子节点，又没有右子节点的时候，就是叶子节点，
因此，如果这个节点称为 node, 那么它应该满足 not node.left and not node.right。

2.需要考虑什么是左叶子节点，那么就要根据这个叶子节点的父节点来进行判断，如果这个叶子节点是父节点的左子节点，那么就满足条件
加到最终的和中。这时候把父节点命名为 node, 如果 if node.left 为真，表示该是父节点的左子节点。
相应地，这时候把1中的判断条件中的 node 替换为 node.left

3.递归深搜每一个节点，如果满足条件，就加入和中，如果节点为空，就返回

"""