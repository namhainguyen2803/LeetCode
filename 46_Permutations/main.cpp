#include <iostream>
#include <vector>
#include <set>
using namespace std;
class Solution {
public:
    struct result_found{};
    set<vector<int>> res;
    bool checkDecrease(vector<int> vect){
        int len = vect.size();
        if(vect.size() == 1){
            return true;
        }
        else if(vect.size() != 1){
            if(vect[0] < vect[1]){
                return false;
            }
            else{
                vector<int> v;
                for(int i = 1;i<len;i++){
                    v.push_back(vect[i]);
                }
                return checkDecrease(v);
            }
        }
    }

    void printVector(vector<int> vect){
        for(auto x: vect){
            cout<<x<<" ";
        }
        cout<<endl;
    }

    void producePermutations(vector<int> vect, vector<int> last_config, int len = 1) {
        // check if the subsequence is in max term or not
        vector<int> checkValid;
        for (int i = 0; i < len; i++) {
            int l = vect.size() - len;
            checkValid.push_back(last_config[l + i]);
        }
        if(checkDecrease(last_config) == true){
            res.insert(last_config);
            throw result_found{};
        }
        else{
            if (checkDecrease(checkValid) == true && checkDecrease(last_config) == false) {

                res.insert(last_config);

                int next_element = last_config[vect.size() - 1 - len]; //3
                int done = 0;
                for (int i = 0; i < len; i++) {
                    int l = vect.size() - len; //3
                    if(next_element > last_config[l+i]){
                        if(l+i-1 == vect.size() - 1 - len){
                            done = 1;
                            producePermutations(vect,last_config,len = len + 1);
                            break;
                        }
                        else{
                            last_config[last_config.size() - 1 - len] = last_config[l+i-1];
                            last_config[l+i-1] = next_element;
                            done = 1;
                            break;
                        }
                    }
                }
                if(done==0){
                    int l = vect.size() - len;
                    last_config[last_config.size() - 1 - len] = last_config[l+len - 1];
                    last_config[l+len - 1] = next_element;

                }
                //sort in increasing order
//                sort(checkValid.begin(), checkValid.end());
                for (int i = 0; i < len/2; i++) {
                    int l = last_config.size()  - len; // l = 4 - len = 4 - 2 = 2
                    int temp = last_config[l + i]; //
                    last_config[l + i] = last_config[l + len - i - 1];
                    last_config[l + len - i - 1] = temp;
                }

                producePermutations(vect,last_config,len = len + 1);
            }

            else if (checkDecrease(checkValid) == false) {
                producePermutations(vect, last_config, len = len - 1);
            }


        }

    }

    vector<vector<int>> permute(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<int> config;
        int len;
        vector<int> last;
        for(int i = 0; i < nums.size();i++){
            last.push_back(nums[i]);
        }
        try {
            producePermutations(nums, last);
        }
        catch (result_found&) {}
        return res;
    }
};
int main() {
    int num;
    cin>>num;

    vector<int> he;
    for(int i=1;i<num+1;i++){
        he.push_back(i);
    }
    Solution hehe;
    vector<vector<int>> haha;
    haha = hehe.permute(he);
    for(auto x: haha){
        for(auto y: x){
            cout<<y<<" ";
        }
        cout<<endl;
    }
    return 0;
}

//Input: nums = [1,2,3]
//Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
