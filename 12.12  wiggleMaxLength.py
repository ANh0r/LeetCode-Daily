class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return 1
        curr_diff=0
        pre_diff=0
        num=1
        for i in range(1,len(nums)):
            curr_diff=nums[i]-nums[i-1]
            if (curr_diff>0 and pre_diff<=0) or (curr_diff<0 and pre_diff>=0):
                num+=1
                pre_diff=curr_diff
        return num