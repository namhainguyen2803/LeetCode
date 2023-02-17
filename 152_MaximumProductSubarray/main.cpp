#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int res;
    int findMax(vector<int> arr){
        int re = arr[0];
        if(arr.size()==1){
            return re;
        }
        else{
            for(int i = 1; i < arr.size();i++){
                if(re < arr[i]){
                    re = arr[i];
                }
            }
            return re;
        }
    }
    void produceMaximumSubarray(vector<int> vect){
        vector<int> dp;
        dp.resize(vect.size());
        dp[0] = vect[0];
        for(int i = 1; i < vect.size(); i++){
            if(dp[i-1]*vect[i] > vect[i]){
                dp[i] = max(dp[i-1]*vect[i],dp[i]);
            }
            else{
                dp[i] = vect[i];
            }
        }
        res = findMax(dp);
    }

    int maxProduct(vector<int>& nums) {
        produceMaximumSubarray(nums);
        return res;
    }
};
int main() {
    Solution sol;
    vector<int> vec;
    int l;
    cin>>l;
    for(int i = 0; i < l; i++){
        int n;
        cin>>n;
        vec.push_back(n);
    }
    cout<<sol.maxProduct(vec);
    return 0;
}
