#include <iostream>
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    queue<TreeNode*> que;
    vector<vector<int>> res;

    vector<vector<int>> levelOrder(TreeNode* root) {
        if(root != nullptr){
            que.push(root);
            map<TreeNode*, int> mp;
            mp.insert({root, 1});
            while(que.size() != 0){

                if(que.front()->left != nullptr){
                    que.push(que.front()->left);
                    mp.insert({que.front()->left, mp[que.front()] + 1});

                }
                if(que.front()->right != nullptr){
                    que.push(que.front()->right);
                    mp.insert({que.front()->right, mp[que.front()] + 1});
                }
                que.pop();
            }
            int i = 1;
            for (auto itr = mp.begin(); itr != mp.end(); ++itr) {
                if(itr->second > res.size()){
                    res.resize(itr->second);
                    res[itr->second - 1].push_back(itr->first->val);
                }
                else{
                    res[itr->second - 1].push_back(itr->first->val);
                }
            }
            return res;
        }
        else{
            return res;
        }
    }
};

int main()
{
    cout<<"Hello World";

    return 0;
}
