# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        if root.children:
            depth_children=[self.maxDepth(node) for node in root.children]
        else:
            return 1
        return max(depth_children)+1
'''
递归DFS：

时间复杂度：我们访问每个节点一次，时间复杂度为 O(N) 。
空间复杂度：最坏情况下，整棵树是非平衡的，例如每个节点都只有一个孩子，递归会调用 N（树的高度）次，因此栈的空间开销是 O(N)。
但在最好情况下，树是完全平衡的，高度只有 log(N)，因此在这种情况下空间复杂度只有 O(log(N)) 。

'''


class Solution2:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        depth = 1
        queue = [(root, depth)]
        while queue:
            root, depth = queue.pop(0)
            if root.children:
                for node in root.children:
                    queue.append((node, depth + 1))
        return depth

'''
法2，迭代法BFS
时间O(N),空间O(N)
'''


class Solution3:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        final_depth=1
        stack=[(root,final_depth)]
        while stack:
            root,depth=stack.pop()
            final_depth=max(final_depth,depth)
            if root.children:
                for node in root.children:
                    stack.append((node,depth+1))
        return final_depth

# 迭代DFS