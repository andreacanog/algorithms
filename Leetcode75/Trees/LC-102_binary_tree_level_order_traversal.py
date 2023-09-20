# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 
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
#  * @return {number[][]}
#  */
var levelOrder = function(root) {
    let res = [];
    let queue = [root];

    while (queue.length) {
        let len = queue.length;
        let level = [];

        for (let i = 0; i < len; i++) {
            let node = queue.shift();

            if (node) {
                levels.push(node);
                queue.push(bode.left);
                queue.push(node.right);
            }
        }

        if (levels.length) {
            res.push(levels);
        }
    }

    return res;
};