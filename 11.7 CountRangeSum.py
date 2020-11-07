class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        N = len(nums)
        if not N : return 0
        snums = [nums[0]] * N
        for i in range(1, N) : snums[i] = nums[i] + snums[i-1]
        snums = sorted(snums)
        res, tot = 0, 0
        for n in nums :
            l, r = bisect.bisect_left(snums, lower) , bisect.bisect_right(snums, upper)
            res = res + (r - l)
            i = bisect.bisect_left(snums, n+tot)
            lower, upper, tot = lower + n, upper + n, tot + n
            del snums[i]
        return res

"""仔细看题。题目只要求我们得到区间的个数，并不需要列出具体的区间。因此累加完后，我们可以把列表进行一次排序，然后会二分查找，找到上下界的位置，它们的差值就是这一轮符合条件的区间的个数。
由于可能存在重叠的数据，所以对于下界我们找左插入点，上界我们找右插入点。
一轮找完，我们立即把这个数抛弃。抛弃之后为了复用累加数组，我们可以从累加数组的每个元素减去这轮被抛弃的数字，但这样又变成了两重循环。为个省去这个循环，我们不减去这个数字，而是把它累加到上下界上，这样只需要更新两个数字，相当于节省了一层循环。

忽略掉前半部分的预处理，主循环的复杂度为：O(n\log n)O(nlogn)。

作者：rockypan
链接：https://leetcode-cn.com/problems/count-of-range-sum/solution/yi-ge-zhi-guan-yi-dong-hao-shi-xian-de-jie-fa-by-r/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""