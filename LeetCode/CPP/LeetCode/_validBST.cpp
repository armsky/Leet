/*
 * Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
*/

#include <climits>
#include <iostream>

//Definition for binary tree
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};



class Solution {
public:
    bool isValidBST(TreeNode *root) {
        if (root == NULL)
          return true;
        return isValidSubTree(root->left, INT_MIN, INT_MAX);
    }

    bool isValidSubTree(TreeNode *node, int min, int max){
        if (node == NULL)
          return true;
       if(node->val > min
                    && node->val < max
                     && isValidSubTree(node->left,min,node->val)
                     && isValidSubTree(node->right,node->val,max))
                return true;
           else
                return false;
    }
};
