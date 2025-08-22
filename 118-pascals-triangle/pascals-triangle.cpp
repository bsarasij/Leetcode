class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> array(numRows);
        for (int i = 0; i < numRows; i++){
            array[i].resize(i+1);
            for (int j = 0; j <= i; j ++){
                if (j == 0){
                    array[i][j] = 1;
                }
                else if (j == i){
                    array[i][j] = 1;
                }
                else{
                    array[i][j] = array[i-1][j-1] + array[i-1][j];
                }
            }
        }
        return array;
    }
};