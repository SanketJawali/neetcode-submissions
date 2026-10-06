/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    private Vector<Integer> res;

    Solution() {
        res = new Vector();
    }

    public List<Integer> inorderTraversal(TreeNode root) {
        if (root == null)
            return res;
        
        dfs(root);
        return res;
    }

    private void dfs(TreeNode node) {
        if (node != null) {
            dfs(node.left);
            res.add(node.val);
            dfs(node.right);
        }
    }
}