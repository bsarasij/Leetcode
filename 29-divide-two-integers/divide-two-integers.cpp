class Solution {
private:
int HALF_INT_MIN = INT_MIN >> 1;
public:
    int divide(int dividend, int divisor) {
        if (dividend == INT_MIN && divisor == -1){
            return INT_MAX;
        } // Edge case

        // Now work in negative domain
        int neg = 2;
        if (dividend > 0){
            neg -= 1;
            dividend = -dividend;
        }
        if (divisor > 0){
            neg -= 1;
            divisor = -divisor;
        }
        // At this point everything is -ve

        int q = 0;
        while (dividend <= divisor){
            int pow = -1;
            int value = divisor;
            while (value > HALF_INT_MIN && value + value >= dividend){
                value += value;
                pow += pow;
            }
            q += pow;
            dividend -= value;
        }
        if (neg != 1){
            q = -q;
        }
        return q;
    }
};