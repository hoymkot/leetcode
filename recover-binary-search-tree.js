

var swap = function ( left, right) {
    temp = left.val
    left.val = right.val
    right.val = temp
}

breakleft = null
breakright = null  
secondHighest = null
highest = null 

var findViolation = function findViolation(root) {
    if (root == null )
        return 

    findViolation(root.left)

    secondHighest = highest
    highest = root

    if (secondHighest != null && secondHighest.val > highest.val) {
        if ( breakleft == null ) {
            breakleft = secondHighest
            breakright = highest
            highest = breakleft
        } else {
            breakright = highest
        }
    }


    findViolation(root.right)
};





/**
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */
var recoverTree = function(root) {
    findViolation(root)
    swap(breakleft, breakright)
    breakleft = null
    breakright = null
    secondHighest = null
    highest = null     
};

