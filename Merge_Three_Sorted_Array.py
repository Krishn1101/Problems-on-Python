"""Given three sorted arrays A, B and C of size N, M and P respectively.
The task is to merge them into a single array which must be sorted in increasing order.

Example 1:

Input: 
N = 4, A[] = [1 2 3 4] 
M = 5, B[] = [1 2 3 4 5] 
P = 6, C[] = [1 2 3 4 5 6]
Output: 1 1 1 2 2 2 3 3 3 4 4 4 5 5 6
Explanation: Merging these three sorted 
arrays, we have: 
1 1 1 2 2 2 3 3 3 4 4 4 5 5 6.
Example 2:

Input: 
N = 2, A[] = [1 2]
M = 3, B[] = [2 3 4] 
P = 4, C[] = [4 5 6 7]
Output: 1 2 2 3 4 4 5 6 7
Explanation: Merging three sorted arrays, 
we have: 1 2 2 3 4 4 5 6 7.

Your Task:
This is a function problem. You only need to complete the function mergeThree() that takes A,B,C as parameters.
The function returns an array or vector."""

                                                #CODE HERE:-

class Solution:
    def mergeThree(self, A,B,C):
        A.extend(B)
        A.extend(C)
        A.sort()
        return A