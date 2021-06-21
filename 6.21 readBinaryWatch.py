class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        table = {0:[],1:[],2:[],3:[],4:[],5:[],6:[]}
        ret = []
        for i in range(60):
            table[bin(i).count('1')].append(i)
        for hour in range(12):
            key = turnedOn-bin(hour).count('1')
            if key < 0 or key > 6 : continue
            for minute in table[key]:
                ret.append(str(hour)+':'+('0' if minute<10 else '')+ str(minute))
        return ret