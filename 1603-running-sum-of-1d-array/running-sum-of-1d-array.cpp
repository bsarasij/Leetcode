class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        if (nums.size() == 1){
            return nums;
        }
        vector<int> cum_sum;
        cum_sum.push_back(nums[0]);
        for (int i = 1; i < nums.size(); i++){
            cum_sum.push_back(cum_sum.back() + nums[i]);
        }    
        return cum_sum;    
    }
};