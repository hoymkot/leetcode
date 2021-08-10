
var result = [] 

var pathSum = function(root, targetSum) {
    trans(root, targetSum, [], 0)
    r = result 
    result = [] 
    return r 
};


var trans = function trans(node, targetSum, parents, current_sum) {
    if ( node == null)
        return 
    current_sum = node.val + current_sum
    if ( current_sum == targetSum ) {
        if (node.left == null && node.right ===null ) {            
            l = [...parents]        
            l.push(node.val)
            result.push(l)
            return
        } 
    } 
    parents.push(node.val) 
    trans(node.left, targetSum, parents, current_sum ) 
    trans(node.right, targetSum, parents, current_sum ) 
    parents.pop()
    
}
