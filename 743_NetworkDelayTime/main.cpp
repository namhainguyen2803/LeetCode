#include <iostream>
#include <vector>

using namespace std;
class PriorityQueue{
public:
    int heap_size;
    vector<vector<int>> data;
    PriorityQueue(){
        vector<int> vect;
        vect.push_back(0);
        vect.push_back(0);
        data.push_back(vect);
        this->heap_size = data.size()-1;
    }
    int parent(int i){
        return (int) i/2;
    }
    int left(int i){
        return 2*i;
    }
    int right(int i){
        return 2*i+1;
    }
    void Insert(vector<int> n){
        data.push_back(n);
        this->heap_size += 1;
    }
    void Min_Heapify(int i){
        int l = left(i);
        int r = right(i);
        int smallest;
        if (l <= this->heap_size && data[l][1] < data[i][1]){
            smallest = l;
        }
        else{
            smallest = i;
        }
        if (r <= this->heap_size && data[r][1] < data[smallest][1]){
            smallest = r;
        }
        if (smallest != i){
            vector<int> tmp = this->data[smallest];
            this->data[smallest] = this->data[i];
            this->data[i] = tmp;
            Min_Heapify(smallest);
        }
    }
    void Build_Min_Heap(){
        int a = (int) this->heap_size/2;
        for (int i=a; i>=1; i--){
            Min_Heapify(i);
        }
    }
    vector<int> extract_min(){
        if (this->heap_size < 1){
            vector<int> vect;
            vect.push_back(-1);
            vect.push_back(-1);
            return vect;
        }
        else if(this->heap_size == 1){
            vector<int> min_element = this->data[1];
            this->data.pop_back();
            this->heap_size -= 1;
            return min_element;
        }
        else{
            vector<int> min_element = this->data[1];
            this->data[1] = this->data[this->heap_size];
            this->data.pop_back();
            this->heap_size = this->heap_size - 1;
            Min_Heapify(1);
            return min_element;
        }
    }
    void Print_Data(){
        cout << "Frontier: ";
        for(int i=1; i<=this->heap_size; i++){
            for(int j=0; j<2; j++){
                cout<<this->data[i][j]<<" ";
            }
            cout<<" , ";
        }
        cout<< endl;
    }
    void Update_Key(int element, int new_weight){
        int idx = 0;
        for(int i = 1; i <= this->heap_size; i ++){
            if (this->data[i][0] == element){
                idx = i;
                break;
            }
        }
        if (this->data[idx][1] > new_weight){
            this->data[idx][1] = new_weight;
            Min_Heapify(idx);
        }
    }
};
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<bool> completed_explored_set;
        vector<bool> visit;
        vector<int> dist;

        for (int i = 0; i<n+1;i++){
            visit.push_back(false);
            completed_explored_set.push_back(false);
            dist.push_back(0);
        }
        PriorityQueue frontier;
        vector<int> vect;
        vect.push_back(k);
        vect.push_back(0);
        frontier.Insert(vect);
        visit[0] = true;
        completed_explored_set[0] = true;
        visit[k] = true;
        int res = -1;
        while (frontier.heap_size != 0){
            frontier.Build_Min_Heap();
//            frontier.Print_Data();
            vector<int> candi = frontier.extract_min();
//            frontier.Print_Data();
            completed_explored_set[candi[0]] = true;

            int current_cost = candi[1];
            dist[candi[0]] = current_cost;
            if (current_cost  > res){
                res = candi[1];
            }

            vector<vector<int>> poss_children = children(times, candi[0]);
            for (int i = 0; i < poss_children.size(); i++){
                if (visit[poss_children[i][1]] == false){
                    vector<int> vect;
                    int cost = poss_children[i][2] + current_cost;
                    vect.push_back(poss_children[i][1]);
                    vect.push_back(cost);
                    frontier.Insert(vect);
                    visit[poss_children[i][1]] = true;
                    dist[poss_children[i][1]] = cost;
                }
                else{
                    int cost = poss_children[i][2] + current_cost;
                    frontier.Update_Key(poss_children[i][1], cost);
                    if (dist[poss_children[i][1]] > cost){
                        dist[poss_children[i][1]] = cost;
                    }
                }
            }
        }
        for(auto x: dist){
            cout<< x<< " ";
        }
        for(int i = 0; i < n+1; i ++){
            if(visit[i] == false){
                return -1;
            }
        }
        return res;
    }
    vector<vector<int>> children(vector<vector<int>>& times, int source_node){
        vector<vector<int>> adjacent_edges;
        int num_edges = times.size();

        for(int i=0; i< num_edges; i++){
            if (times[i][0] == source_node){
                adjacent_edges.push_back(times[i]);
            }
        }
        return adjacent_edges;
    }

};

int main() {
    Solution sol;
    vector<vector<int>> arr;
    int n;
    int k;
    for (int i = 0; i < 4; i ++){
        vector<int> r;
        for(int j = 0; j < 3; j ++){
            int t;
            cin >> t;
            r.push_back(t);
        }
        arr.push_back(r);
    }
    cin >> n;
    cin >> k;
    cout << sol.networkDelayTime(arr, n, k);
    return 0;
}


