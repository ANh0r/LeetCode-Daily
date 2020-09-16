"""翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
"""
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.right,root.left = left,right

        return root

    '''
    这个题能够很好地帮助我们理解递归。

递归函数本身也是函数，调用递归函数就把它当做普通函数来看待，
一定要只思考当前层的处理逻辑，明白该递归函数的输入输出是什么即可，调用的时候不要管函数内部实现。
不要用肉脑 debug 递归函数的调用过程，会被绕进去。

首先来分析invertTree(TreeNode root)函数的定义：

函数的定义是什么？
该函数可以翻转一棵二叉树，即将二叉树中的每个节点的左右孩子都进行互换。
函数的输入是什么？
函数的输入是要被翻转的二叉树。
函数的输出是什么？
返回的结果就是已经翻转后的二叉树。
然后我们来分析函数的写法：

递归终止的条件
当要翻转的节点是空，停止翻转，返回空节点。
返回值
虽然对 root 的左右子树都进行了翻转，但是翻转后的二叉树的根节点不变，故返回 root 节点。
函数内容
root 节点的新的左子树：是翻转了的 root.right => 即 root.left = invert(root.right);
root 节点的新的右子树：是翻转了的 root.left => 即 root.right = invert(root.left);
至此，递归函数就写完了。在『函数内容』编写的时候，是不是把递归函数invertTree(TreeNode root)当做了普通函数来用？调用invertTree(TreeNode root)函数就是能实现翻转二叉树的目的，不需要理解函数内部怎么实现的。

最后，提醒大家避免踩一个小坑，不能直接写成下面这样的代码：


root.left = invert(root.right)
root.right = invert(root.left)
这是因为第一行修改了root.left，会影响了第二行。在 Python 中，正确的写法是把两行写在同一行，就能保证 root.left 和 root.right 的修改是同时进行的。

作者：fuxuemingzhu
链接：https://leetcode-cn.com/problems/invert-binary-tree/solution/di-gui-han-shu-zen-yao-xie-ben-wen-bang-zhu-ni-li-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''