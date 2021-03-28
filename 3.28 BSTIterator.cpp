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
class BSTIterator {
private:
    vector<TreeNode*> S;
public:
    BSTIterator(TreeNode* root){
        while(root){
            S.push_back(root);
            root = root->left;
        }
    }
    int next() {
        TreeNode* t = S.back();
        S.pop_back();
        int val = t->val;
        t = t->right;
        while(t){
            S.push_back(t);
            t = t->left;
        }
        return val;
    }
    bool hasNext() {
        return !S.empty();
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */