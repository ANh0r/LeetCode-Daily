class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int i = 1;
        int len = nums.size();
        int res_tmp;
        for(i = 1; i < len; i++){
            if(nums[i] < nums[i-1]) break;
        }
        vector<int> tmp;
        for(int j = 0; j < len; j++){
            tmp.push_back(nums[(i+j)%len]);
        }
        //return tmp[0];
        return divide_search(tmp, target);


    }
    bool divide_search(vector<int> nums, int target) {
        int l = 0;
        int r = nums.size() - 1;
        int mid;
        while(l < r){
            mid = (l + r)/2;
            if(nums[mid] == target)
                return true;
            else if(nums[mid] < target)
                l = mid+1;
            else if(nums[mid] > target)
                r = mid;
        }
        mid = (l + r)/2;
        return nums[mid]==target;
    }
};