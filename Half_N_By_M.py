"""Given two values N and M. Give the value when N is halved M-1 times.

Example 1:

Input: N = 100, M = 4
Output: 12
Explaination: The sequence of numbers is 
100, 50, 25, 12.
Example 2:

Input: N = 10, M = 5
Output: 0
Explaination: The sequence is 10, 5, 2, 1 and 0."""

                            #CODE HERE:- 

class Solution:
    def mthHalf(self, N, M):
        for i in range(1,M):
            N = N//2
        return N