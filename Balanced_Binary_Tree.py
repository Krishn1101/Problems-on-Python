"""Given a binary tree, determine if it is height-balanced.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true"""

                    #CODE HERE:-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = True
    def height(self,root):
        #base case:-
        if root == None:
            return 0
        #recursive case:-
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        if abs(leftHeight-rightHeight)>1:
            self.ans = False
        return max(leftHeight,rightHeight) + 1

    def isBalanced(self,root):
        self.height(root)
        return self.ans