class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = []                                                  # 结果列表
        cur = [root]                                                # 接下来要循环的当前层节点，存的是节点
        while cur:                                                  # 当前层存在结点时
            cur_layer_val = []                                      # 初始化当前层结果列表为空，存的是val
            next_layer_node = []                                    # 初始化下一层结点列表为空
            for node in cur:                                        # 遍历当前层的每一个结点
                if node:                                            # 如果该结点不为空，则进行记录
                    cur_layer_val.append(node.val)                  # 将该结点的值加入当前层结果列表的末尾
                    next_layer_node.extend([node.left, node.right]) # 将该结点的左右孩子结点加入到下一层结点列表
            if cur_layer_val:                                       # 只要当前层结果列表不为空
                queue.insert(0, cur_layer_val)                      # 则把当前层结果列表插入到队列首端
            cur = next_layer_node                                   # 下一层的结点变成当前层，接着循环
        return queue                                                # 返回结果队列

'''给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

'''
"""levelOrder = list()
if not root:
    return levelOrder

q = collections.deque([root])
while q:
    level = list()
    size = len(q)
    for _ in range(size):
        node = q.popleft()
        level.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    levelOrder.append(level)

return levelOrder[::-1]
"""