class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        int inf = 1e4;
        vector <int> d (n, inf);
        d[k-1] = 0;
        for (int i = 0; i < n-1; i++){
            for (vector <int> edge : times){
                int u = edge[0]-1;
                int v = edge[1]-1;
                int w = edge[2];
                if (d[u] != inf && d[u] + w < d[v]){
                    d[v] = d[u] + w;
                }
            }
        }
        int maxDelay = *max_element(d.begin(), d.end());
        return (maxDelay == inf) ? -1 : maxDelay;    }
};