"""There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible."""

                                                            #CODE HERE:-

class Queue:
    def __init__(self):
        self.q = []
        self.front = -1
        
    def push(self,x):
        if self.front == -1:
            self.front = 0
        self.q.append(x)
    
    def pop(self):
        if self.front == -1:
            return -1
        x = self.q[self.front]
        self.front+=1
        if len(self.q) == self.front:
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
    def canFinish(self,numCourses,prerequisites):
        q = Queue()
        ans = []
        indegree = [0]*numCourses

        adjList = []
        for i in range(numCourses):
            adjList.append([])
        
        for a,b in prerequisites:
            #b->a
            indegree[a]+=1
            adjList[b].append(a)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                ans.append(i)
                q.push(i)
        
        while q.size()>0:
            front = q.pop()
            for x in adjList[front]:
                indegree[x]-=1
                if indegree[x]==0:
                    ans.append(x)
                    q.push(x)
        if len(ans) == numCourses:
            return True
        else:
            return False