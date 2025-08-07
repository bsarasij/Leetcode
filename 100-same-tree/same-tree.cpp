/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool inorder_compare(TreeNode* node1, TreeNode* node2){
        if (!node1){
            if (!node2){
                return true;
            }
            return false;
        }
        if (!node2){
            return false;
        } 
        if (node1 -> val != node2 -> val){
            return false;
        }
        bool left_comp = inorder_compare(node1-> left, node2 -> left);
        bool right_comp = inorder_compare(node1-> right, node2 -> right);
        return left_comp && right_comp;
    }
    bool isSameTree(TreeNode* p, TreeNode* q) {
        
        return  inorder_compare(p, q);
    }
};