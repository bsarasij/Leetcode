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
    bool traverse(TreeNode* node, int remainder){
        if (!node){
            return false;
        }
        if (!node -> left && !node -> right){
            return (remainder == node -> val);
        }
        return traverse(node ->left, remainder - node -> val) || traverse(node -> right, remainder - node -> val);

    } 
    bool hasPathSum(TreeNode* root, int targetSum) {
        
        return traverse(root, targetSum);
    }
};