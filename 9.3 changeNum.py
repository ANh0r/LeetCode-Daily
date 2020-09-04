from typing import List


class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0] = numbers[0] + numbers[1]  #设num[0], num[1]分别为x，y
        numbers[1] = numbers[0] - numbers[1]  # 实际等于x， num[0] 此时等于x+y
        numbers[0] = numbers[0] -numbers[1]
        return numbers

    """或者异或：
        numbers[0] = numbers[0] ^ numbers[1];
        numbers[1] = numbers[0] ^ numbers[1];
        numbers[0] = numbers[0] ^ numbers[1];
        return numbers
    """