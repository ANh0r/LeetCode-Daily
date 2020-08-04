class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        fz = 1  # 分子
        fm = cont[-1]  # 分母

        for i in reversed(range(len(cont) - 1)):
            fz = fm * cont[i] + fz  # 分子分母互换：因为是1/fz/fm ——> fm/fz
            fz, fm = fm, fz

        return [fm, fz]

# def fraction(self, cont: List[int]) -> List[int]:
# A = cont[::-1]
# fz = 1
# fm = A[0]
# if fm == 0:
#     return Null
# for x in range(1,len(A)):
#     fz = fm * A[x] + fz
#     fz, fm = fm, fz
# fz, fm = fm, fz
# return [fz,fm]


#  看来还得重新学习下小学数学，nmd原来1/分数 -> 分数的倒数这种东西好长时间才反应过来 唉

