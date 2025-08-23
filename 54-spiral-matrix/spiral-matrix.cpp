class Solution {
public:
    void trav_right(const int& x_min, const int& y_min, const int& y_max, vector<vector<int>>& matrix, vector<int>& spiral_mat){
        if (y_min > y_max){
            return;
        }
        for (int j = y_min; j <= y_max; j++){
            spiral_mat.push_back(matrix[x_min][j]);
        }
    }
    void trav_down(const int& y_max, const int& x_min, const int& x_max, vector<vector<int>>& matrix, vector<int>& spiral_mat){
        if (x_min > x_max){
            return;
        }
        for (int i = x_min; i <= x_max; i++){
            spiral_mat.push_back(matrix[i][y_max]);
        }

    }
    void trav_left(const int& x_max, const int& y_max, const int& y_min, vector<vector<int>>& matrix, vector<int>& spiral_mat){
        if (y_min > y_max){
            return;
        }
        for (int j = y_max; j >= y_min; j--){
            spiral_mat.push_back(matrix[x_max][j]);
        }
    }
    void trav_up(const int& y_min, const int& x_max, const int& x_min, vector<vector<int>>& matrix, vector<int>& spiral_mat){
        if (x_min > x_max){
            return;
        }
        for (int i = x_max; i >= x_min; i--){
            spiral_mat.push_back(matrix[i][y_min]);
        }
    }

    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<int> spiral_mat;
        int x_min = 0;
        int x_max = m-1;
        int y_min = 0;
        int y_max = n-1;
        while (x_min <= x_max && y_min <= y_max){
            if (x_min == x_max){
                trav_right(x_min, y_min, y_max, matrix, spiral_mat);
                break;
            }
            if (y_min == y_max){
                trav_down (y_max, x_min, x_max, matrix,  spiral_mat);
                break;
            }
            else {
                trav_right(x_min, y_min, y_max, matrix, spiral_mat);
                trav_down (y_max, x_min + 1, x_max, matrix,  spiral_mat);
                trav_left (x_max, y_max-1, y_min, matrix, spiral_mat);
                trav_up (y_min, x_max-1, x_min+1, matrix, spiral_mat);
            }    
            x_min += 1;
            x_max -= 1;
            y_min += 1;
            y_max -= 1;            
        }
        return spiral_mat;
    }
};