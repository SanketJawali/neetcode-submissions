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
    public TreeNode insertIntoBST(TreeNode root, int val) {
        // Trace the tree to find the position of the val
        // If current node's value is higher, search in left subtree
        // else in right subtree
        // If no left/right subtree, create a new node and point current nodes's ptr to it
        TreeNode curr = root;
        TreeNode newnode = new TreeNode(val);
        while (curr != null) {
            if (curr.val > val) {
                if (curr.left == null) {
                    curr.left = newnode;
                    break;
                }
                curr = curr.left;
            } else {
                if (curr.right == null) {
                    curr.right = newnode;
                    break;
                }
                curr = curr.right;
            }
        }

        return root != null ? root : newnode;
    }
}