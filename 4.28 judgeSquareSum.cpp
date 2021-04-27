class Solution {
public:
    bool judgeSquareSum(int c) {
        // 注意c的范围2的31次方！
        long long right = sqrt(c);
        long long left = 0;
        // 双指针相向而行
        while(left <= right) {
            // 如果相等，返回为真
            if(left * left + right * right == c) {
                return true;
            } else if(left * left + right * right < c) {
                left ++;
            } else right --;
        }
        return false;
    }
};