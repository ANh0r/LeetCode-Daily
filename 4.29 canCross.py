class Solution:
    def canCross(self, stones: List[int]) -> bool:

        if stones[1] - stones[0] > 1: return False

        stonesSet = set(stones)  # 变成Set， 加速检索

        @functools.lru_cache(None)  # 加上备忘录，去掉重复计算
        def helper(i, step):
            # 状态，表示当前是第几块石头，是走几步走过来的。
            if i == stones[-1]:
                return True

            # 选择， 走 step + 1 步， 走 step 步，还是走step - 1 步？，
            # 只要往前走的步数有石头（在数组内），就试着可以往前走
            if i + step + 1 in stonesSet:
                if helper(i + step + 1, step + 1):
                    return True

            if i + step in stonesSet:
                if helper(i + step, step):
                    return True

            if step - 1 > 0 and i + step - 1 in stonesSet:
                # 这边要检查一下，step -1 要大于0 才走
                if helper(i + step - 1, step - 1):
                    return True

            return False

        return helper(stones[1], stones[1] - stones[0])