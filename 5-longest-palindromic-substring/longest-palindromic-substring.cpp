class Solution {
public:
    bool palin(int i, int j, string& s, vector<vector<int>>& memo) {
        if (i >= j) return true;
        if (memo[i][j] != -1) return memo[i][j];

        memo[i][j] = (s[i] == s[j]) && palin(i + 1, j - 1, s, memo);
        return memo[i][j];
    }

    string longestPalindrome(string s) {
        int n = s.size();
        vector<vector<int>> memo(n, vector<int>(n, -1)); // -1 = uncomputed
        string result = "";

        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (palin(i, j, s, memo)) {
                    int len = j - i + 1;
                    if (len > result.size()) {
                        result = s.substr(i, len);
                    }
                }
            }
        }

        return result;
    }
};
