/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */
var flatten = function(root) {
    trans(root)
};

var trans = function trans(node) {
    if (node == null)
        return null
    
    var right = node.right
    if (node.left != null ) {        
        node.right = node.left
        node.left = null
    } 
    if (node.right == null) {
        return node 
    }
    else {                
        var last = trans(node.right)
        if (right == null || right == node.right) 
            return last 
        else {
            last.right = right 
            return trans(last.right)
        } 
        
    }
}
