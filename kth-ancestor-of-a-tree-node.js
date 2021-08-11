var TreeAncestor = function(n, parent) {
    this.n = n
    this.parent = parent
    this.lookup = {}
    
};

TreeAncestor.prototype.dp = function(i, j) {
    if ( i == -1) 
        return -1 
    if (j == 0 ) 
        return this.parent[i]
    if (this.lookup[i]===undefined)
        this.lookup[i] = {} 
    if ( this.lookup[i][j] === undefined)
        return this.lookup[i][j] = this.dp(this.dp(i, j-1), j-1) 
    else
        return this.lookup[i][j]
}




TreeAncestor.prototype.getKthAncestor = function(node, k) {
    if (node < 0 || node >= this.n) 
        return -1
    if (k < 1 || k >= this.n) 
        return -1

    t = k
    nd = node
    while (t != 0) {
        p = Math.floor(Math.log2(t))
        nd = this.dp(nd, p)
        t = t - 2**p
    }
    return nd
};
