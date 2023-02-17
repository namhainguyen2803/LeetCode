#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
class Solution {
public:
    vector<vector<int>> res;

    void CS(vector<int> repeat, vector<int> not_repeat, unordered_map<int, int> umap, vector<int> potential, int targ, int sum=0, int ind=0){
        for(int i = ind; i < not_repeat.size(); i++){
            sum = sum + not_repeat[i];
            if(sum < targ){
                if(umap[not_repeat[i]] != 1){
                    umap[not_repeat[i]] = umap[not_repeat[i]] - 1;
                    potential.push_back(not_repeat[i]);
                    for(auto x: potential){
                        cout<<"1: "<<x<<" ";
                    }
                    cout<<endl;
                    CS(repeat, not_repeat, umap, potential, targ, sum, ind = i);
                    sum = sum - not_repeat[i];
                    potential.pop_back();
                }
                else if(umap[not_repeat[i]] == 1){
                    if(i == not_repeat.size() - 1){
                        for(auto x: potential){
                            cout<<"2: "<<x<<" ";
                        }
                        cout<<endl;
                        break;
                    }
                    else if(i != not_repeat.size() - 1){
                        potential.push_back(not_repeat[i]);
                        for(auto x: potential){
                            cout<<"3: "<<x<<" ";
                        }
                        cout<<endl;
                        CS(repeat, not_repeat, umap, potential, targ, sum, ind = i + 1);
                        sum = sum - not_repeat[i];
                        potential.pop_back();
                        continue;
                    }
                }

            }
            else if(sum > targ){
                potential.push_back(not_repeat[i]);
                for(auto x: potential){
                    cout<<"4: "<<x<<" ";
                }
                cout<<endl;
                potential.pop_back();
                break;
            }
            else if(sum == targ){
                potential.push_back(not_repeat[i]);
                for(auto x: potential){
                    cout<<"5: "<<x<<" ";
                }
                cout<<endl;
                res.push_back(potential);
                break;
            }
        }
    }


    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<int> po;
        sort(candidates.begin(),candidates.end()); // sort in increasing order of candidates


        unordered_map<int, int> ump; // dictionary containing number of occurrence of elements in candidates
        int cnt = 1;
        if(candidates.size() != 1){
            for(int i=1;i<candidates.size();i++){
                int a = candidates[i];
                if(a == candidates[i-1]){
                    if(i != candidates.size()-1){
                        cnt += 1;
                    }
                    if(i == candidates.size()-1){
                        cnt += 1;
                        ump.insert({candidates[i],cnt});
                    }
                }
                else if(a != candidates[i-1]){
                    if(i != candidates.size()-1){
                        ump.insert({candidates[i-1],cnt});
                        cnt = 1;
                    }
                    else if(i == candidates.size()-1){
                        ump.insert({candidates[i-1],cnt});
                        ump.insert({candidates[i],1});
                    }
                }
            }
        }

        else if(candidates.size() == 1){
            ump.insert({candidates[0],1});
        }


        vector<int> vect; // vector containing unique elements in candidates
        for(auto x: ump){
            vect.push_back(x.first);
        }
        sort(vect.begin(),vect.end());
        CS(candidates, vect, ump,  po, target);
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
    haha = hehe.combinationSum2(he,tar);
    for(auto x: haha){
        for(auto y: x){
            cout<<y<<" ";
        }
        cout<<endl;
    }
    return 0;
}
