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
    int traverse(TreeNode* node){
        if (!node){
            return 0;
        }
        int left = traverse(node -> left);
        if (left == -1){
            return -1;
        }
        int right = traverse(node -> right);
        if (right == -1){
            return -1;
        }
        if (std::abs(left - right) > 1) {
            return -1;
        }
        return 1 + std::max(left, right); 
    }
    bool isBalanced(TreeNode* root) {
        if (!root){
            return true;
        }
        return traverse(root) != -1;
    }
};