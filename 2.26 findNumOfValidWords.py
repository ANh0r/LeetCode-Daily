class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        fre = {}
        for w in words:
            mask = 0
            for ch in w:
                mask |= (1 << (ord(ch)-ord('a')))
            if str(mask).count('1') <= 7:
                fre[mask] = fre.get(mask,0)+1
        ans = []
        for p in puzzles:
            mask = 0
            cnt = 0
            for i in range(1,7):
                mask |= (1 << (ord(p[i])-ord('a')))
            sub = mask
            while sub:
                s = sub | (1 << (ord(p[0]) - ord("a")))
                if s in fre:
                    cnt += fre[s]
                sub = (sub-1) & mask
            if (1 << (ord(p[0]) - ord("a"))) in fre:
                cnt += fre[1 << (ord(p[0]) - ord("a"))]


            ans.append(cnt)
        return ans