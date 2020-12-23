class Solution:
    def firstUniqChar(self, s: str) -> int:
        dct = {}
        for ch in s:
            dct[ch] = dct.get(ch, 0) + 1
        for i in dct.keys():
            if dct[i] == 1:
                return s.find(i)
        return -1
"""position = dict()
n = len(s)
for i, ch in enumerate(s):
    if ch in position:
        position[ch] = -1
    else:
        position[ch] = i
first = n
for pos in position.values():
    if pos != -1 and pos < first:
        first = pos
if first == n:
    first = -1
return first"""