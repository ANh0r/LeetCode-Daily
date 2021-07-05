class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # 倒着的时候， 记录map，乘的基数，迭代中的乘数，个数，个数的10进制位数，元素
        cnts, multiply, muls, num, num_count, atom = defaultdict(int), 1, [], 0, 0, ""
        for c in formula[::-1]:
            if c == ')':
                # 如果当前有统计的数字，乘的基数要叠加
                if num:
                    multiply *= num
                    muls.append(num)
                    num = num_count = 0
                else:
                    muls.append(1)
            elif c == '(':
                # 去除掉上一个乘数
                multiply //= muls.pop()
            elif str.isdigit(c):
                num += int(c) * (10 ** num_count)
                num_count += 1
            elif str.islower(c):
                atom += c
            else:
                atom += c
                # 注意我们在更新元素个数时，始终要考虑乘的基数
                if num:
                    cnts[atom[::-1]] += num * multiply
                else:
                    cnts[atom[::-1]] += multiply
                atom = ""
                num = num_count = 0
        return "".join(key if cnts[key] == 1 else key + str(cnts[key]) for key in sorted(cnts.keys()))