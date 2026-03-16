"""Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]"""

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
    def averageOfLevels(self, root):
        ans = []
        if root == None:
            return ans
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
                avg = sum(level)/len(level)
                ans.append(avg)
        return ans