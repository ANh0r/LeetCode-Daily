class Solution {
public:
    string largestNumber(vector<int>& nums) {
        if(nums.empty()) return "";
        if(nums.size() == 1) return to_string(nums[0]);

        sort(nums.begin(), nums.end(), comparison); // 调用STL中的sort函数
        string result = "";
        for(int i : nums)
        {
            result += to_string(i);
        }
        if(result[0] == '0') return "0"; // 特殊case，全是0的时候应该输出0而不是00000
        return result;
    }
    static bool comparison(const int& a, const int& b)
    {
        // 注：a和b也可以不用传引用（即 &）
        // 注：此处要用static，因为std::sort是属于全局的，无法调用非静态成员函数，而静态成员函数或全局函数是不依赖于具体对象，可以独立访问。
        // 也可以把comparison这个函数放在Solution这个class的外面，但是记住一定要放在整个class的上面而不能是下面。
        // 不然代码里调用sort函数时会找不到comparison，而导致报错。
        string concatenation1 = to_string(a) + to_string(b);
        string concatenation2 = to_string(b) + to_string(a);

        return concatenation1 > concatenation2;
    }
};
//之所以要用static关键字，是因为如果是在class内部，
//是需要通过对象名.comparion()这种方式来调用的，但是这里我们没有对象，也就是写不出对象名.comparion()这种形式，
//所以只能使用static，这样就可以直接调用了。更具体的解释可以看这个：由LeetCode C++ sort函数第三个参数cmp必须声明为static 引发的思考
//
/*class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> strNums(nums.size());
        for (auto i = 0; i < nums.size(); ++i) {
            strNums[i] = to_string(nums[i]);
        }

        sort(strNums.begin(), strNums.end(), compare);
        string ans;
        for (const auto& strNum : strNums) {
            ans += strNum;
        }

        if (ans.length() > 0 && ans[0] == '0') {
            return "0";
        }

        return ans;
    }

private:
    static bool compare(const string& str1, const string& str2)
    {
        int length1 = str1.size();
        int length2 = str2.size();

        int length = min(length1, length2);
        auto i = 0;
        while (i < length) {
            if (str1[i] != str2[i]) {
                return str1[i] > str2[i];
            }

            ++i;
        }

        string compare1 = str1 + str2;
        string compare2 = str2 + str1;

        return compare1 > compare2;
    }
};*/