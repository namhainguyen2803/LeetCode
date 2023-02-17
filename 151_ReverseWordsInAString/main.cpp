#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> res;
    void parseString(string s){
        string word;
        for(auto ch: s){
            if(ch == ' '){
                if(word.size() != 0){
                    res.push_back(word);
                    word.clear();
                    continue;
                }
                else{
                    continue;
                }
            }
            else{
                word.push_back(ch);
            }
        }
        if(word.size() != 0){
            res.push_back(word);
        }
    }

    string reverseWords(string s) {
        parseString(s);
        string result;
        for(int i= res.size()-1;i>0;i--){
            result = result + res[i] + ' ';
        }
        result = result + res[0];
        return result;
    }
};
int main() {
    Solution sol;
    string s;
    getline(cin,s);
    string result = sol.reverseWords(s);
    cout<<result;
    return 0;
}
