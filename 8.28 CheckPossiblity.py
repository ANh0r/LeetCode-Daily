"""给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。

 

示例 1:

输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。

"""


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
                if i+1 < len(nums) and i-2 >= 0:
                    if nums[i+1] < nums[i-1] and nums[i-2] > nums[i]:
                        return False
            if count > 1:
                return False
        return True

"""解题思路：
遍历数组，初始count = 0，如果当前元素值比它下一个元素值大，则count += 1，当count > 1时，直接返回false。
另外，在遍历数组的过程中，如果遇到 “特殊情况”，可以直接返回false；当循环正常结束则返回true。
特殊情况解释：
首先看一个简单的例子：[2, 4, 0, 1]

当下标 i == 2 时，nums[i] < nums[i-1]，也就是 0 < 4，这时我们要保证数组非递减有两种选择：

选择 1：把 0 放大，并且保证 0 后面的数不能比 4 小，0 前面的数均是非递减的；

选择 2：把 4 缩小，并且保证 4 前面的数不能比 0 大，4 后面的数均是非递减的。

换言之，当 0 < 4时，如果以上两个选择中的保证同时不满足，说明该数组肯定无法通过只修改一个元素而变为非递减数组，该情况即为上述提到的 “特殊情况”。对于本例，有：当 0 < 4时，0 后面的数为 1，1 小于 4，不满足选择 1 的保证；且 4 前面的数为 2，4 后面的数为 0，0 小于 2，不满足选择 2 的保证。

综上，我们可以把 “特殊情况” 归纳为：


if nums[i] < nums[i-1]:          # 当 0 < 4 时
    if nums[i+1] < nums[i-1] and nums[i-2] > nums[i]:         # 1 < 4 and 2 > 0
        return False             # 不用继续遍历，可直接返回false
另外需要注意数组下标不要越界。

复杂度分析：
时间复杂度 O(N): 遍历整个数组耗费的时间，N 为数组长度。

空间复杂度 O(1): 使用的额外空间为常数级别。

作者：han-han-a-gou
链接：https://leetcode-cn.com/problems/non-decreasing-array/solution/python3xiang-jie-bu-gai-bian-shu-zu-yuan-su-zhi-ch/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""