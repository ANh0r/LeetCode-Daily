class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table = [defaultdict(int) for _ in range(501)]
        foods = set()
        for cos, t, food in orders:
            table[int(t)][food] += 1
            foods.add(food)
        foods = sorted(list(foods))
        ans = [["Table"] + foods]
        for i in range(1, 501):
            if table[i]:
                tmp = [str(i)]
                for food in foods:
                    tmp.append(str(table[i][food]))
                ans.append(tmp)
        return ans 