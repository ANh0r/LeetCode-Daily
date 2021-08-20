class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        left, mid, right = 0, k, 2 * k                  # 初始化左中右指针
        res = ''                                        # 初始化结果字符串
        while len(res) < len(s):                        # 满足条件时执行
            res += s[left:mid][::-1] + s[mid:right]     # 把当前单元的结果添加到结果字符串
            left, mid, right = left + 2 * k, mid + 2 * k, right + 2 * k
        return res                                      # 返回结果