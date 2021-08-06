/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */



var lessThan = function ( val, lst) {
    for (const i of lst) {
        if (val >= i )
            return false
    }
    return true
}

var greaterThan = function ( val, lst) {
    for (const i of lst) {
        if (val <= i )
            return false
    }
    return true
}

var validBST = function validBST(root, left=[], right = [] ) {
    if (root == null )
        return true
    if (root.left == null && root.right == null)
        return lessThan(root.val, left) && greaterThan(root.val, right) 
    left.push(root.val)
    if ( validBST(root.left, left, right) == false )
        return false
    left.pop()
    right.push(root.val)
    if ( validBST(root.right, left, right) == false )
        return false
    right.pop()
    return lessThan(root.val, left) && greaterThan(root.val, right) 

};




/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function isValidBST(root) {
    return validBST(root)
};


