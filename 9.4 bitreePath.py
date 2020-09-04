# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        path = []
        if root.left:
            for i in self.binaryTreePaths(root.left):
                path.append(str(root.val)+'->'+i)
        if root.right:
            for i in self.binaryTreePaths(root.right):
                path.append(str(root.val)+'->'+i)
        return path
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