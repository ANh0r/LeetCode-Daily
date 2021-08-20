class Solution:
    def compress(self, chars: List[str]) -> int:
        pre, count = chars[0], 1
        n = len(chars)
        i, j = 1, 0
        while i < n:
            ch = chars[i]
            i += 1
            if pre != ch:
                chars[j] = pre
                j += 1
                if count > 1:
                    cnt = str(count)
                    for k in cnt:
                        chars[j] = k
                        j += 1
                count = 1
                pre = ch
            else:
                count += 1
        chars[j] = pre
        j += 1
        if count > 1:
            cnt = str(count)
            for k in cnt:
                chars[j] = k
                j += 1
        return j