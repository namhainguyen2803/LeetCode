#include <iostream>
#include <vector>
#include <string>
using namespace std;
class Solution {
public:
    vector<vector<int>> res;

    void CS(vector<int> can, vector<int> potential, int targ, int sum=0, int ind=0){
        for(int i=ind;i<can.size();i++){
            sum += can[i];
            if(sum == targ){ //target configuration
                potential.push_back(can[i]);
                res.push_back(potential);
//                cout<<"Hang chuan: ";
//                for(auto x: potential){
//                    cout<<x<<" ";
//                }
//                cout<<endl;
//                cout<<"Sum la: "<<sum<< endl;
                break;
            }
            else if(sum > targ){ //incorrect configuration
//                potential.push_back(can[i]);
//                cout<<"Hang loi: ";
//                for(auto x: potential){
//                    cout<<x<<" ";
//                }
//                cout<<endl;
//                cout<<"Sum la: "<<sum<< endl;
//                potential.pop_back();
                break;
            }
            else if(sum < targ){ //in process to produce configuration
                potential.push_back(can[i]);
                CS(can,potential,targ,sum,ind=i);
                sum = sum - can[i];
                potential.pop_back();
                continue;
            }
        }
    }



    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> po;
//        vector<int> qu;
        CS(candidates,  po, target);
        return res;
    }
};
int main() {
    vector<int> he;
    int num;
    int tar;
    vector<int> h;

    cin>>num;
    for(int i=0;i<num;i++){
        int can;
        cin>>can;
        he.push_back(can);
    }

    cin>>tar;

    Solution hehe;
    vector<vector<int>> haha;
    haha = hehe.combinationSum(he,tar);
    for(auto x: haha){
        for(auto y: x){
            cout<<y<<" ";
        }
        cout<<endl;
    }
    return 0;
}
