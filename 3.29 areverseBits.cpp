class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t rev = 0;
        for (int i = 0; i < 32 && n > 0; ++i) {
            rev |= (n & 1) << (31 - i);
            n >>= 1;
        }
        return rev;
    }
};
// 答案每次左移 所求数字每次右移 n的最后一位是我们想要的添加进答案的
//n: 10001111101010
//rev:01010111110001
//n末位是0 添加进rev中，rev此时为0，n右移1000111110101
//n末位是1，添加进rev中作为第二位，注意当rev为0时候需要左移使1加到0的右边
//循环