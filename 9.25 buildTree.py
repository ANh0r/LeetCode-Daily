class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # 实际上inorder 和 postorder一定是同时为空的，因此你无论判断哪个都行
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        i = inorder.index(root.val)
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])

        return root
"""后序遍历是左右根，因此postorder最后一个元素一定整个树的根。由于题目说明了没有重复元素，因此我们可以通过val去inorder找到根在inorder中的索引i。
而由于中序遍历是左根右，我们容易找到i左边的都是左子树，i右边都是右子树。

我使用红色表示根，蓝色表示左子树，绿色表示右子树

作者：fe-lucifer
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/solution/si-lu-qing-xi-dai-ma-jian-ji-he-105ti-si-lu-yi-zhi/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""