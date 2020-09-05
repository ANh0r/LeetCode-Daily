# forDefinition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root == None:
            return []

        def dfs(root):
            if root == None:
                return []
            if not root.left and not root.right:
                return [str(root.val)]

            return [str(root.val) + "->" + i for i in dfs(root.left) + dfs(root.right)]

        return dfs(root)
    '''# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        def dfs(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    res.append(path)
                else:
                    path += '->' 
                    dfs(root.left, path)
                    dfs(root.right, path)

        res = []
        dfs(root, '')
        return res'''

"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3


"""