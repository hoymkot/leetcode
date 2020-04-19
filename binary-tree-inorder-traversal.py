# https://leetcode.com/problems/binary-tree-inorder-traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if (root == None):
            return [];
        p = [];
        stack = [root.right,root.val, root.left];
        while len(stack) > 0:
            node = stack.pop();
            if node != None:
                if (isinstance(node, TreeNode)):
                    stack.append(node.right);                
                    stack.append(node.val);
                    stack.append(node.left);                
                else:
                    p.append(node);
        return p; 
       # return self.inorderTraversal(root.left) +[root.val] + self.inorderTraversal(root.right);
                
