class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        if (stones.size() == 1){
            return stones[0];
        }
        priority_queue<int> heap;
        for (int stone: stones){
            heap.push(stone);
        }
        while(heap.size() >= 2){
            int big1 = heap.top();
            heap.pop();
            int big2 = heap.top();
            heap.pop();
            if(big1 != big2){
                heap.push(big1 - big2);
            }
        }
        return heap.empty() ? 0 : heap.top();
    }
};