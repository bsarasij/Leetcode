class Solution {
public:
    bool isBalanced(string num) {
        int sign = 1;
        int diff = 0;
        for (int i = 0; i < num.size(); i++){
            diff += sign*(num[i] - '0');
            sign *= -1; 
        }
        return diff == 0;
    }
};