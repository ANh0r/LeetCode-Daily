class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    temp = nums[i]
                    nums[i], nums[temp] = nums[temp], nums[i]


'''
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''解法一：排序
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        pre = nums[0]
        n = len(nums)
        for index in range(1, n):
            if pre == nums[index]:
                return pre
            pre = nums[index]
         
时间：O nlogn
空间：O 1   
            '''

'''解法二:集合/字典
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        repeatDict = {}
        # 此处可以换成set集合 
        #repeatDict = set()
        for num in nums:
            if num not in repeatDict:
                repeatDict[num] = 1
            #for i in range (len(nums))
            #repeatDict.add(nums[i])
            #if len(data_set) < i+1:
            #   return nums[i]
            else:
                return num
双O(n)
                '''

'''解法三:原地排序
解释：时间O(n),空间O(1),修改原数据。因为所有的元素都小于len(nums),所以可以让位置i放置元素值i，
果位置i的元素值不是i，则可以交换nums[i]与nums[nums[i]],这样nums[i]的值就被正确归位了，
继续交换直到位置[i]也被正确交换了。如果我们发现nums[i]与nums[nums[i]]的值一致，则发现了重复的元素，
返回即可。针对性较强，普适性较弱。时间复杂度的算法：因为每交换一次数组位置，至少有一个元素被放到了该元素值对应的下标的位置，
至多2个，所有有n个元素，最坏的考虑就是需要操作n次。所以是O(n)
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    # 注意，不可用nums[i], nums[nums[i]] == nums[nums[i]], nums[i]来实现数据交换
                    # 这和python底层实现有关，详见以下网页：
                    # https://blog.csdn.net/qq_43029747/article/details/95992657
                    temp = nums[i]
                    nums[i], nums[temp] = nums[temp], nums[i]
'''

'''解法四：二分查找
该方法对于本题不适用，但是题目类似，长度为n的数组，且数字都在1~n-1之间，且一定有数字是重复的。
每一遍二分的过程，统计nums元素中1~m的数量(m <=n-1, 改变m的值，遍历的是整个数组)，如果数量大于这个值，这说明重复的元素一定在1~m中。
但实际此种方法不可行，例如[1, 1, 1, 2, 4, 5, 6, 7, 8, 9]，对这个样例，则无法找到正确的答案。
(本题不使用）
class Solution:
    def findRepeatNumber(self, nums:List[int]) -> int:
        # 注意初始值是1
        min_value = 1
        max_value = len(nums) - 1
        while (max_value > min_value):
            mid_value = (max_value + min_value) // 2
            counts = self.countNums(nums, min_value, mid_value);
            if counts > mid_value - min_value + 1:
                max_value = mid_value
            else:
                # 注意这个地方需要加1，不然最后会陷入死循环，比如最后max_value为2,min_value为1，则会一直循环,对应的上面也可以给max_value复制的地方减1
                min_value = mid_value + 1
        # 跳出循环的条件一定是max_value = min_value
        return min_value

    def countNums(self, nums, min_value, max_value):
        count = 0
        for ele in nums:
            if min_value <= ele <= max_value:
                count += 1
        return count'''