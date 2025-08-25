class Solution {
public:
    vector<int> kWeakestRows(
        vector<vector<int>>& mat, int k
        ) {
        std::unordered_map<int, int> map;
        std::priority_queue<pair<int,int>> heap;
        for (int row = 0; row < mat.size(); row++){
            map[row] = std::accumulate(mat[row].begin(), mat[row].end(), 0);
        }
        for (auto& row: map){
            heap.push({row.second, row.first});    
            if (heap.size() > k){
                heap.pop();
            }
        };
        vector<int> weakRows;

        while(!heap.empty()){
            weakRows.push_back(heap.top().second);
            heap.pop();
        }
        reverse(weakRows.begin(), weakRows.end());
        return weakRows;
    }
};