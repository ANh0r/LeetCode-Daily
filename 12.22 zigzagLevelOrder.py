# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.answer = list()

        def dfs(root, level):
            if not root:
                return

            if len(self.answer) < level + 1:
                self.answer.append([])

            self.answer[level].append(root.val)

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        print(self.answer)

        for item in range(1, len(self.answer), 2):
            self.answer[item].reverse()

        return self.answer
"""res = []

if root is None:
    return res

q = deque()
q.append(root)
depth = 1

while q:
    sub_res = []

    for _ in range(len(q)):
        e = q.popleft()
        sub_res.append(e.val)
        if e.left is not None:
            q.append(e.left)
        if e.right is not None:
            q.append(e.right)

    if depth % 2 == 0:
        sub_res.reverse()

    res.append(sub_res)
    depth += 1

return res"""