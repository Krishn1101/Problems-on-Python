"""Given a positive integer, n. Find the factorial of n.

Examples :

Input: n = 5
Output: 120
Explanation: 1 x 2 x 3 x 4 x 5 = 120
Input: n = 4
Output: 24
Explanation: 1 x 2 x 3 x 4 = 24"""

                    #CODE HERE:-

class Solution:
    def factorial(self, n):
        if(n==0 or n==1):
            return 1
        else:
            return((n)*(self.factorial(n-1)))