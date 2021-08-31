class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1,version2=version1.split('.'),version2.split('.')
        for i in range(len(version1)):
            version1[i]=int(version1[i])
        for i in range(len(version2)):
            version2[i]=int(version2[i])
        if len(version1)<=len(version2):
            version1+=[0]*(len(version2)-len(version1))
        else:
            version2+=[0]*(len(version1)-len(version2))
        for i in range(len(version1)):
            if version1[i]>version2[i]:
                return 1
            if version2[i]>version1[i]:
                return -1
        return 0