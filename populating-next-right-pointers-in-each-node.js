
var connect = function(root) {
    if (root != null) {
        trans(root,0, {})
        root.next = null
    }
    return root
    
};

var trans = function(node, level, rights){
    if ( node == null){
        return 
    }
    trans(node.right, level+1, rights)

    if (rights[level] === undefined){
        rights[level] = null
    } 
    
    node.next= rights[level]        
    
    rights[level] = node 
    trans(node.left, level+1, rights)
}
