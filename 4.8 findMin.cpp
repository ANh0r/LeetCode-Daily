class Solution {
public:
    int findMin(vector<int>& nums) {
        int n = nums.size();
        int l = 0, r = nums.size();

        if (nums[0] < nums[n - 1]) return nums[0];  //数组完全有序，则返回第一个元素

        while (l < r)
        {
            int mid = (l + r) >> 1;
            if (nums[mid] <= nums.back()) r = mid;  //将中间值与数组末尾元素比较
            else l = mid + 1;
        }

        return nums[l];
    }
};