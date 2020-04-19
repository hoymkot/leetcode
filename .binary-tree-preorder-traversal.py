# https://leetcode.com/problems/binary-tree-preorder-traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if (root == None):
            return [];
        p = [root.val];
        stack = [ root.right, root.left];
        while len(stack) > 0:
            node = stack.pop();
            if node != None:
                p = p + [node.val]
                stack.append(node.right);                
                stack.append(node.left);                
        return p;
        
        
