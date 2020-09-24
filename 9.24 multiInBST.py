# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def findMode(self, root: TreeNode) -> List[int]:
            if not root:
                return []
            hash = defaultdict(int)

            def dfs(root):
                if not root:
                    return
                hash[root.val] += 1
                dfs(root.left)
                dfs(root.right)

            dfs(root)
            ma = max(hash.values())
            return [key for key, val in hash.items() if val == ma]

        '''def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = []
        cnt, max_cnt, last = 0, 0, None
        for v in inorder(root):
            if v == last:
                cnt += 1
            else:
                cnt = 1
            if cnt > max_cnt:
                ans = [v]
            elif cnt == max_cnt:
                ans.append(v)
            max_cnt = max(max_cnt, cnt)
            last = v
        return ans
'''

    """BST的中序遍历有序，返回最多元素的数组
    傻逼
    众数和有序没序都没有什么关系，直接遍历取出到hash表中找到最多的元素
    """