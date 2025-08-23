class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.size() == 1){
            return intervals;
        }
        vector<vector<int>> merged_arr;
        std::sort(intervals.begin(), intervals.end());
        for (const std::vector<int>& entry: intervals){
            if (merged_arr.empty()){
                merged_arr.push_back(entry);
            }
            else {
                vector<int>& last =  merged_arr.back();
                if (entry[0] > last[1]){
                    merged_arr.push_back(entry);
                } 
                else {
                    if (entry[1] > last[1]){
                        last[1] = entry[1];
                    }
                }
            }
        }
        return merged_arr;
    }
};