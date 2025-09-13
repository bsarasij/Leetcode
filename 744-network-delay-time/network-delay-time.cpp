class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
       using pr = pair<int, int>;
        unordered_map<int, vector<pr>> adj;
        for (vector<int>& time : times){
            int first = time[0];
            int second = time[1];
            int delay = time[2];
            adj[first].push_back({second, delay});
            // adj[second].push_back({first, delay});
        }
        priority_queue<pr, vector<pr>, greater<pr>> heap;
        vector<int> delay(n, INT_MAX);
        delay[k-1] = 0;
        heap.push({0,k});
        while(!heap.empty()){
            pr top = heap.top();
            heap.pop();
            int curr_delay = top.first;
            int source = top.second;
            for (auto& [nbr, weight]: adj[source]){
                if (weight + curr_delay < delay[nbr-1]){
                    delay[nbr-1] = weight + curr_delay;
                    heap.push({delay[nbr-1], nbr});
                }
            }  
        }
        int max_delay = *max_element(delay.begin(), delay.end());
        for (int i : delay){
            cout << i << endl;
        }
        
        return (max_delay!= INT_MAX) ? max_delay : -1;
    }
};