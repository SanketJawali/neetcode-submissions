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
    private int target;

    public TreeNode removeLeafNodes(TreeNode root, int t) {
        target = t;

        return dfs(root) ? null : root;
    }

    private boolean dfs(TreeNode node) {
        // Return true if value of children node == target
        // else return false
        if (node == null) {
            return false;
        }

        // Visit left subtree
        boolean l = dfs(node.left);
        boolean r = dfs(node.right);

        if (l) 
            node.left = null;
        if (r) 
            node.right = null;

        if (node.left == null && node.right == null) {
            // Current node is leaf
            return node.val == target;
        }
        return false;
    }
}