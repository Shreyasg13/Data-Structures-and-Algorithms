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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        
       if(p == NULL && q == NULL) //if both are null
            return true; 
        
        else if( (p == NULL || q == NULL)) //if one of the node is null
            return false; 
        
         else if ( p->val!=q->val ) //if one of the node is different 
            return false;
                
        return isSameTree(p->left,q->left) && isSameTree(p->right,q->right);
        
    }
};