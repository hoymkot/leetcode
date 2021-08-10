var maxPathSum = function(root) {
    maxSum = Number.MIN_SAFE_INTEGER
    trans(root)
    return maxSum
};

var maxSum = 0
const max = (a, b ) => a > b ? a : b
var trans = function (node) {
    if (node == null)
        return 0 
    const left = trans(node.left) 
    const right = trans(node.right)
    const cur = node.val
    const l = [cur, cur+left, cur+right, cur+left+right ]
    maxSum = max(maxSum, l.reduce(max))
    const ul = [cur, cur+left, cur+right] 
    return ul.reduce(max)
}
