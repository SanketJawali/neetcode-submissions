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
    private int count = 0;
    public int goodNodes(TreeNode root) {
        dfs(root, root.val);
        return count;
    }

    private void dfs(TreeNode node, int currmax) {
        if (node == null)
            return;
        if (node.val >= currmax) {
            count++;
        }
        dfs(node.left, Math.max(currmax, node.val));
        dfs(node.right, Math.max(currmax, node.val));
    }
}
