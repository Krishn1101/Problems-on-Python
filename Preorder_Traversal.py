"""Given the root of a binary tree, your task is to return its Preorder traversal.

Note: A preorder traversal first visits the node, then visits the left child (including its entire subtree), and finally visits the right child (including its entire subtree).

Examples:

Input: root = [1, 4, N, 4, 2]
   
Output: [1, 4, 4, 2]
Explanation: The preorder traversal of the given binary tree is [1, 4, 4, 2]
Input: root = [6, 3, 2, N, 1, 2, N]
    
Output: [6, 3, 1, 2, 2] 
Explanation: The preorder traversal of the given binary tree is [6, 3, 1, 2, 2]"""

                                                        #CODE HERE:-


# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = []
        
    def preorder(self,root):
        if root is None:
            return
        self.ans.append(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
    def preOrder(self, root):
        self.ans = []
        self.preorder(root)
        return self.ans