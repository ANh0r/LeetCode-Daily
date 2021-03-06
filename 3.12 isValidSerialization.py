class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        degree = 1
        for node in preorder.split(','):
            if degree == 0:
                return False
            if node == '#':
                degree -= 1
            else:
                degree += 1
        return degree == 0

"""
把此问题中的空节点理解成叶子节点。

可以理解成是节点数问题，叶子节点数总是比非叶子节点数多一。根据前序遍历过程，先遍历的非叶子节点数总是比叶子节点数多。

也可以理解为出度入度相等问题：我命名有问题，根结点的入度为0出度为2，其他非叶子结点的入度为1出度为2，叶子节点入度为1出度为0。因为根节点多出来一个出度，所以初始化度为1，一个非叶子节点时度+1，加入一个空节点（叶子节点）时度-1，如果度为0，即达到出度入度相等，已经形成一颗二叉树。
例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。

给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。

每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。

你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如 "1,,3" 。
"""
