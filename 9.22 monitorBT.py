"""给定一个二叉树，我们在树的节点上安装摄像头。

节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。

计算监控树的所有节点所需的最小摄像头数量。

 

示例 1：



输入：[0,0,null,0,0]
输出：1
解释：如图所示，一台摄像头足以监控所有节点。
示例 2：



输入：[0,0,null,0,null,0,null,null,0]
输出：2
解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(root: TreeNode) -> List[int]:
            if not root:
                return [float("inf"), 0, 0]

            la, lb, lc = dfs(root.left)
            ra, rb, rc = dfs(root.right)
            a = lc + rc + 1
            b = min(a, la + rb, ra + lb)
            c = min(a, lb + rb)
            return [a, b, c]

        a, b, c = dfs(root)
        return b
"""本题以二叉树为背景，不难想到用递归的方式求解。本题的难度在于如何从左、右子树的状态，推导出父节点的状态。

为了表述方便，我们约定：如果某棵树的所有节点都被监控，则称该树被「覆盖」。

假设当前节点为 \textit{root}root，其左右孩子为 \textit{left}, \textit{right}left,right。如果要覆盖以 \textit{root}root 为根的树，有两种情况：

若在 \textit{root}root 处安放摄像头，则孩子 \textit{left}, \textit{right}left,right 一定也会被监控到。此时，只需要保证 \textit{left}left 的两棵子树被覆盖，同时保证 \textit{right}right 的两棵子树也被覆盖即可。
否则， 如果 \textit{root}root 处不安放摄像头，则除了覆盖 \textit{root}root 的两棵子树之外，孩子 \textit{left}, \textit{right}left,right 之一必须要安装摄像头，从而保证 \textit{root}root 会被监控到。
根据上面的讨论，能够分析出，对于每个节点 \textit{root}root ，需要维护三种类型的状态：

状态 aa：\textit{root}root 必须放置摄像头的情况下，覆盖整棵树需要的摄像头数目。
状态 bb：覆盖整棵树需要的摄像头数目，无论 \textit{root}root 是否放置摄像头。
状态 cc：覆盖两棵子树需要的摄像头数目，无论节点 \textit{root}root 本身是否被监控到。
根据它们的定义，一定有 a \geq b \geq ca≥b≥c。

对于节点 \textit{root}root 而言，设其左右孩子 \textit{left}, \textit{right}left,right 对应的状态变量分别为 (l_a,l_b,l_c)(l 
a
​	
 ,l 
b
​	
 ,l 
c
​	
 ) 以及 (r_a,r_b,r_c)(r 
a
​	
 ,r 
b
​	
 ,r 
c
​	
 )。根据一开始的讨论，我们已经得到了求解 a,ba,b 的过程：

a = l_c + r_c + 1a=l 
c
​	
 +r 
c
​	
 +1
b = \min(a, \min(l_a + r_b, r_a + l_b))b=min(a,min(l 
a
​	
 +r 
b
​	
 ,r 
a
​	
 +l 
b
​	
 ))
对于 cc 而言，要保证两棵子树被完全覆盖，要么 \textit{root}root 处放置一个摄像头，需要的摄像头数目为 aa；要么 \textit{root}root 处不放置摄像头，此时两棵子树分别保证自己被覆盖，需要的摄像头数目为 l_b + r_bl 
b
​	
 +r 
b
​	
 。

需要额外注意的是，对于 \textit{root}root 而言，如果其某个孩子为空，则不能通过在该孩子处放置摄像头的方式，监控到当前节点。因此，该孩子对应的变量 aa 应当返回一个大整数，用于标识不可能的情形。

最终，根节点的状态变量 bb 即为要求出的答案。
"""