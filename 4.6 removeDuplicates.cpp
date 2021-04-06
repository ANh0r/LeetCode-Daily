class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        if (n < 2){
            return n;
        }

        int slow = 2;
        int fast = 2;
        while (fast < n ){
            if (nums[slow - 2 ] == nums[fast]){
                fast++ ;
                continue;
            }else{
                nums[slow] = nums[fast];
                slow++;
                fast++;
            }

    }
    return slow;
    }
};