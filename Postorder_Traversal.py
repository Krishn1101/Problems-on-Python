"""Given the root of a Binary Tree, your task is to return its Postorder Traversal.

Note: A postorder traversal first visits the left child (including its entire subtree), then visits the right child (including its entire subtree), and finally visits the node itself.

Examples:

Input: root = [19, 10, 8, 11, 13]

Output: [11, 13, 10, 8, 19]
Explanation: The postorder traversal of the given binary tree is [11, 13, 10, 8, 19].
Input: root = [11, 15, N, 7]
 
Output: [7, 15, 11]
Explanation: The postorder traversal of the given binary tree is [7, 15, 11]."""

                                                    #CODE HERE:-


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = []
    def postorder(self,root):
        if root is None:
            return
        
        self.postorder(root.left)
        self.postorder(root.right)
        self.ans.append(root.data)
    def postOrder(self, root):
        self.ans = []
        self.postorder(root)
        return self.ans