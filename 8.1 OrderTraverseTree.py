class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lastTreeNodeInBST(self, root: TreeNode, k: int) -> TreeNode:
        ans = []
        def inOrderTraverse(root):
            if root is None:
                return None
            inOrderTraverse(root.left)
            ans.append(root.val)
            inOrderTraverse(root.right)
        return ans


t = Solution()
a = TreeNode([1, 2, 3, 4, 5, 6, 7])
print(t.lastTreeNodeInBST(a, 1))
