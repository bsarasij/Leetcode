class Solution {
public:
    int LIS(int i, vector<int>& nums, std::unordered_map<int, int>& memo, int n){
        if (i == n-1){
            return 1;
        }
        int max_len = 0;
        if (!memo.contains(i)){
            int max_len_j = 0;
            for(int j = i + 1; j < n; j++){
                if (nums[j] > nums[i]){
                    max_len_j = max(max_len_j,LIS(j, nums, memo, n));
                }
            }
            max_len = max(max_len,1 + max_len_j);
            memo[i] = max_len; 
        }
        return memo[i];
    }
    int lengthOfLIS(vector<int>& nums) {
        std::unordered_map<int, int> memo;
        int n = nums.size();
        int result = 0;
        for (int i = n -1 ; i >= 0; i--) {
            result = max(result, LIS(i, nums, memo,n));
        }
        return result;
    }
};