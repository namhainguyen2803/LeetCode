#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int num_nodes = graph.size();
        int arr_coloring[num_nodes];
        arr_coloring[0] = 1;
        for(int i = 1; i < num_nodes; i++){
            arr_coloring[i] = 0;
        }
        for(int i = 0; i < num_nodes; i++){
            for(int j = 0; j < graph[i].size(); j ++){
                if(arr_coloring[graph[i][j]] == 0){
                    arr_coloring[graph[i][j]] == 1;
                }
                else{
                    if(arr_coloring[graph[i][j]] == arr_coloring[i]){
                        return false;
                    }
                }
            }
        }
        return true;
    }
};
int main() {
    Solution sol;

    return 0;
}
