"""Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4."""

                                    #CODE HERE:-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def check(self, root, mn, mx):
        if root is None:
            return True
        if root.val<mn or root.val>mx:
            return False
        checkLeft = self.check(root.left,mn,root.val-1)
        checkRight = self.check(root.right,root.val+1,mx)

        return checkLeft and checkRight
    def isValidBST(self,root):
        return self.check(root,-1000000000000,1000000000000)