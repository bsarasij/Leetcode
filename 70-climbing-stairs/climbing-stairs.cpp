class Solution {
public:
    int climb(int n, std::unordered_map<int, int> &memo){
        if (n <= 2){
            return n;
        }
        if (!memo.contains(n)){
            memo[n] = climb(n-1, memo) + climb(n-2, memo);
        } 
        return memo[n];
    }
    int climbStairs(int n) {
        std::unordered_map<int, int> memo;
        return climb(n, memo);
    }
};