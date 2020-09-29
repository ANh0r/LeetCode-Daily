"""
二叉树的后序遍历
"""
# 迭代1：前序遍历最常用模板（后序同样可以用）


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        # # # 前序迭代模板：最常用的二叉树DFS迭代遍历模板
        # while stack:
        #     cur = stack.pop()
        #     res.append(cur.val)
        #     if cur.right:
        #         stack.append(cur.right)
        #     if cur.left:
        #         stack.append(cur.left)
        # return res

        # # 后序迭代，相同模板：将前序迭代进栈顺序稍作修改，最后得到的结果反转
        while stack:
            cur = stack.pop()
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
            res.append(cur.val)
        return res[::-1]