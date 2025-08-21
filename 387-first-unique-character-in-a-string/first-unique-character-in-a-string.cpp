class Solution {
public:
    int firstUniqChar(string s) {
        std::unordered_map<char, int> idx;
        int ans = INT_MAX;
        for (int i = 0; i < s.size(); i++){
            if (idx.find(s[i]) == idx.end()){
                idx[s[i]] = i;
            }
            else{
                idx[s[i]] = INT_MAX; 
            }
        }
        for (std::pair<char, int> i: idx){
            ans = min(ans, i.second);
        }
        return (ans == INT_MAX) ? -1 : ans;

    }
};