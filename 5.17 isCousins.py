class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # x 的信息
        x_parent, x_depth, x_found = None, None, False
        # y 的信息
        y_parent, y_depth, y_found = None, None, False

        def dfs(node: TreeNode, depth: int, parent: TreeNode):
            if not node:
                return

            nonlocal x_parent, y_parent, x_depth, y_depth, x_found, y_found

            if node.val == x:
                x_parent, x_depth, x_found = parent, depth, True
            elif node.val == y:
                y_parent, y_depth, y_found = parent, depth, True

            # 如果两个节点都找到了，就可以提前退出遍历
            # 即使不提前退出，对最坏情况下的时间复杂度也不会有影响
            if x_found and y_found:
                return

            dfs(node.left, depth + 1, node)

            if x_found and y_found:
                return

            dfs(node.right, depth + 1, node)

        dfs(root, 0, None)
        return x_depth == y_depth and x_parent != y_parent