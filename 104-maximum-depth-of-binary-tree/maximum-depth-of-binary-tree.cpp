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
        if(!node){
            return 0;
        }
        return 1 + std::max(traverse(node -> left), traverse(node -> right)); 
    }
    int maxDepth(TreeNode* root) {
        if (!root){
            return 0;
        }    
        int left_counter = traverse (root -> left);
        int right_counter = traverse (root -> right);
        return 1 + std::max(left_counter, right_counter);
    }
};