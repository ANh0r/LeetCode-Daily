
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''left = 0
        right = len(numbers)-1
        while left < right:
            if numbers[left]+ numbers[right] == target :
                return [left+1,right+1]
            elif numbers[left]+ numbers[right]<target:
                left = left + 1
            else:
                right = right - 1''''''
        暴力解法
        index=[]
        for i in range(0,len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    index.append(i)
                    index.append(j)
                    break
        return index
        '''
        #哈希表
        dict={}
        #dict['num']=i
        for index,num in enumerate(numbers):
            #target_num=target-num
            if num in dict:
                return [dict[num]+1,index+1]
            dict[target-num]=index