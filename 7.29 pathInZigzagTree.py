class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        while label != 1:
            res.append(label)
            label >>= 1
            # 这里我采用异或实现
            label = label ^(1 << (label.bit_length() - 1)) - 1
        return [1]+res[::-1]