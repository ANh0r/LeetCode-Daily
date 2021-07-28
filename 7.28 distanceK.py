# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        stack = deque()
        def bt(node):
            stack.append(node)
            if node.val == target.val:
                return True
            if node.left and bt(node.left):
                return True
            if node.right and bt(node.right):
                return True
            stack.pop()
        bt(root)
        while len(stack) > k+1:
            stack.popleft()
        ans = []
        if len(stack) == k+1:
            ans.append(stack.popleft().val)
        q = deque()
        for i in range(len(stack)):
            node = stack[i]
            if i == len(stack)-1:
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            else:
                if node.left and node.left!=stack[i+1]:
                    q.append(node.left)
                elif node.right and node.right!=stack[i+1]:
                    q.append(node.right)
            m = i + k - len(stack)
            while m>0 and len(q)>0:
                n = len(q)
                while n>0:
                    node = q.popleft()
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                    n -= 1
                m-=1
            while len(q)>0:
                ans.append(q.pop().val)
        return ans