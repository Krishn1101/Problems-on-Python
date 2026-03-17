"""Given the root of a binary Tree. Your task is to return the right view of the binary tree. The right view of a Binary Tree is the set of nodes visible when the tree is viewed from the right side.

Examples :

Input: root = [1, 2, 3, N, N, 4, 5]
     2_2
Output: [1, 3, 5]
Input: root = [1, 2, 3, 4, N, N, N, N, 5]
     Right-view-in-binary-tree-1
Output: [1, 3, 4, 5]"""

                                                        #CODE HERE:-


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


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
    def rightView(self, root):
        ans = []
        if root == None:
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
                ans.append(level[-1])
        return ans