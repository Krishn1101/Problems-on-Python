"""Given the root of a binary tree. Your task is to return the left view of the binary tree. The left view of a binary tree is the set of nodes visible when the tree is viewed from the left side.

Note: If the tree is empty, return an empty list.

Examples :

Input: root = [1, 2, 3, 4, 5, N, N]

Output:[1, 2, 4]
Explanation: From the left side of the tree, only the nodes 1, 2, and 4 are visible.

Input: root = [1, 2, 3, N, N, 4, N, N, 5, N, N]

Output: [1, 2, 4, 5]
Explanation: From the left side of the tree, only the nodes 1, 2, 4, and 5 are visible."""

                                                    #CODE HERE:-

 
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None 

class Queue:
    def __init__(self):
        self.q = []
        self.front = -1
    
    def push(self,x):
        if self.front == -1:
            self.front+=1
        self.q.append(x)
    def pop(self):
        if len(self.q) == 0:
            return -1
        x = self.q[self.front]
        self.front+=1
        if self.front == len(self.q):
            self.front = -1
            self.q = []
        return x
    def getFront(self):
        if len(self.q) == 0:
            return -1
        return self.q[self.front]
    def size(self):
        if self.front == -1:
            return 0
        return len(self.q) - self.front
class Solution:
    def leftView(self, root):
        ans = []
        if root is None:
            return ans
        queue = Queue()
        
        queue.push(root)
        ans.append(root.data)
        
        while queue.size()>0:
            level = []
            l = queue.size()
            for i in range(l):
                front = queue.pop()
                if front.left!=None:
                    queue.push(front.left)
                    level.append(front.left.data)
                if front.right!=None:
                    queue.push(front.right)
                    level.append(front.right.data)
            if len(level)>0:
                ans.append(level[0])
        return ans