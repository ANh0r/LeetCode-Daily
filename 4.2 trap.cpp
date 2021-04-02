class Solution {
public:
     int trap(vector<int>& height) {
        int left = 0;
        int right = height.size()-1;
        int left_max = 0;
        int right_max =0;
        int ans = 0;

        while (left<= right){
            //只要右边有比左边高，无论中间是什么情况，当前所能存的雨水只和左边的最高相关.
            if(left_max<right_max){
                ans +=max(0,left_max-height[left]);
                left_max = max(left_max,height[left]);
                left++;
            }else{
                ans +=max(0,right_max-height[right]);
                right_max = max(right_max,height[right]);
                right--;
            }
        }
        return ans;
    }
};