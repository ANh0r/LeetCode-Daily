class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def dfs(root):
            nonlocal res, pre
            if not root:
                return
            dfs(root.left)
            if pre != -1:
                res = min(res, root.val - pre)
            pre = root.val
            dfs(root.right)

        pre = -1
        res = float('inf')
        dfs(root)
        return int(res)


'''
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

 

示例：

输入：

   1
    \
     3
    /
   2

输出：
1

解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。

思路：
BST中序遍历有序，任意两节点差的绝对值必然在相邻接点，只需要遍历相邻节点的差然后取最小值。
'''