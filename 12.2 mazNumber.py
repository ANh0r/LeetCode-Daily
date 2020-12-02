class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        """
        题目要求我们用num1和 num2组成k位最大数字，我们可以取num1的可以形成i位最大数字，num2的k - i位最大数字，他们再组成数字就是最大的。这里有个问题，如何求解一个数组的i位最大数字，例如如何找出[6, 0, 4]最大的两位数字？

方法，我们使用单调栈，维护一个单调减的数组即可！
        """

        def getMaXArr(nums, i):
            if not i:
                return []
            # pop表示最多可以不要nums里几个数字，要不组成不了i位数字
            stack, pop = [], len(nums) - i
            for num in nums:
                while pop and stack and stack[-1] < num:
                    pop -= 1
                    stack.pop()
                stack.append(num)
            return stack[:i]

        def merge(tmp1, tmp2):
            return [max(tmp1, tmp2).pop(0) for _ in range(k)]

        res = [0] * k
        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                # 取num1的i位, num2的k - i
                tmp1 = getMaXArr(nums1, i)
                tmp2 = getMaXArr(nums2, k - i)
                # 合并
                tmp = merge(tmp1, tmp2)
                if res < tmp:
                    res = tmp
        return res
    # 上面一个可以一句话写成
    # return max(merge(getMaXArr(nums1, i), getMaXArr(nums2, k - i)) for i in range(k + 1) if i <= len(nums1) and k - i <= len(nums2))
