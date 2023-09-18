# /**
#  * Definition for a binary tree node.
#  * function TreeNode(val, left, right) {
#  *     this.val = (val===undefined ? 0 : val)
#  *     this.left = (left===undefined ? null : left)
#  *     this.right = (right===undefined ? null : right)
#  * }
#  */
# /**
#  * @param {TreeNode} root
#  * @return {TreeNode}
#  */

var invertTree = function(root) {
    if (!root) return root;

    let leftNode = invertTree(root.left);
    let rightNode = invertTree(root.right);

    root.left = leftNode
    root.right = rightNode
    retunr node 
}