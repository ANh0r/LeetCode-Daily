class Solution {
public:
    bool isUgly(int n) {
        if(n<=0) return false;
        vector<int> ugly = {2,3,5};
        for (int ugly: ugly){
            while (n%ugly ==0)
            n/=ugly;
        }
        return n==1;

    }
};