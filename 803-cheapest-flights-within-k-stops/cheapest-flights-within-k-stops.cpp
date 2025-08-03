class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        static const int inf = 1e6;
        vector<int> d (n,inf);

        d[src] = 0;
        for (int i = 0; i<= k; ++i){
            vector<int> temp = d;
            for (int j = 0; j < flights.size(); j++){
                if (d[flights[j][0]]!= inf && d[flights[j][0]] + flights[j][2] < temp[flights[j][1]]){
                    temp[flights[j][1]] = d[flights[j][0]]+flights[j][2];
                }
            }
            d = temp;
        }
        // for (int i = 0; i < d.size(); i++) {
        //     cout << d[i] << " ";
        // }
        return d[dst] == inf ? -1 : d[dst];
    }
    
};