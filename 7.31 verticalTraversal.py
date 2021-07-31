# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        stack, d = [(root, 0, 0)], defaultdict(list)
        while stack:
            node, x, y = stack.pop()
            if node:
                d[x].append((y, node.val))
                stack.extend([(node.right, x+1, y+1), (node.left, x-1, y+1)])
        return [[val for _, val in sorted(d[x])] for x in sorted(d)]