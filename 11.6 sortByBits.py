def count1(x):
    cnt = 0
    while x:
        x &= x - 1
        cnt += 1
    return cnt

"""
统计1的个数
 return sorted(arr, key=lambda x:(bin(x).count("1"), x))
"""