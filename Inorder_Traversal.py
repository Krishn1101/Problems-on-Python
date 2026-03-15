"""Given a root of a Binary Tree, your task is to return its Inorder Traversal.

Note: An inorder traversal first visits the left child (including its entire subtree), then visits the node, and finally visits the right child (including its entire subtree).

Examples:

Input: root = [1, 2, 3, 4, 5]
            
Output: [4, 2, 5, 1, 3]
Explanation: The inorder traversal of the given binary tree is [4, 2, 5, 1, 3].
Input: root = [8, 1, 5, N, 7, 10, 6, N, 10, 6]
              
Output: [1, 7, 10, 8, 6, 10, 5, 6]
Explanation: The inorder traversal of the given binary tree is [1, 7, 10, 8, 6, 10, 5, 6]."""

                                                    #CODE HERE:-


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = []
    
    def inorder(self,root):
        if root is None:
            return
        
        self.inorder(root.left)
        self.ans.append(root.data)
        self.inorder(root.right)
    def inOrder(self, root):
        self.ans = []
        self.inorder(root)
        return self.ans
        