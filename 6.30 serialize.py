# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.res = ''

        def dfs(root: TreeNode):
            if not root:
                self.res += 'None' + ','
                return
            self.res += str(root.val) + ','
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')

        def dfs():
            a = data.pop(0)
            if a == 'None':
                return None
            root = TreeNode(int(a))
            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()