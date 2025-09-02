class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        int m = min (n, k);
        using Node = tuple<int,int,int>;

        priority_queue<Node, vector<Node>, greater<Node>> heap;
        for (int i = 0; i < m; i++){
            heap.push(std::make_tuple(matrix[i][0], i, 0));
        }
        for (int p = 1; p <= k-1; p++){
            Node top = heap.top();
            int r = std::get<1>(top);
            int c = std::get<2>(top);
            heap.pop();
            if (c+1 < n ){
                heap.push(std::make_tuple(matrix[r][c+1], r, c+1));
            }

        }
        return std::get<0>(heap.top());
    }
};