# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        """
        给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)
        使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

 

        例如：
        
        输入: 原始二叉搜索树:
                      5
                    /   \
                   2     13
        
        输出: 转换为累加树:
                     18
                    /   \
                  20     13


        """
'''思路:
1.BST 中序遍历（是排序好从小到大）
2.反过来，从到小
3.累加
def dfs(root: TreeNode):
            nonlocal total
            if root:
                dfs(root.right)
                total += root.val
                root.val = total
                dfs(root.left)
        
        total = 0
        dfs(root)
        return root
'''
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode):
            nonlocal total_tem
            if root:
                dfs(root.right)
                total_tem = root.val
                root.val = total_tem
                dfs(root.left)
        total_tem = 0
        dfs(root)
        return root


"""以右->根->左的顺序遍历二叉树，将遍历顺序的前一个结点的累加值记录起来，和当前结点相加，得到当前结点的累加值。"""
"""今天晚上or明天写一个LeetCode的链表转二叉树的数据结构
恶心心"""





