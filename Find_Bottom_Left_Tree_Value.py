"""Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

Example 1:


Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7"""

                                        #CODE HERE:-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Queue:
    def __init__(self):
        self.q = []
        self.front = -1

    def push(self,x):
        if self.front == -1:
            self.front += 1
        self.q.append(x)

    def pop(self):
        if len(self.q)==0:
            return -1
        x = self.q[self.front]
        self.front+=1
        if self.front == len(self.q):
            self.front = -1
            self.q = []
        return x
    
    def getFront(self):
        if len(self.q)==0:
            return -1
        
        return self.q[self.front]
    
    def size(self):
        if self.front == -1:
            return 0
        
        return len(self.q) - self.front

class Solution:
    def findBottomLeftValue(self,root):
        ans = []
        if root == None:
            return ans
        if root.left == None and root.right == None:
            return root.val
        queue = Queue()

        queue.push(root)
        ans.append(root.val)

        while queue.size()>0:
            level = []
            l = queue.size()
            for i in range(l):
                front = queue.pop()
                if front.left!=None:
                    queue.push(front.left)
                    level.append(front.left.val)
                if front.right!=None:
                    queue.push(front.right)
                    level.append(front.right.val)
            if len(level)>0:
                ans.append(level)
        return ans[-1][0]