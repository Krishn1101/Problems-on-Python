"""Given an integer n, calculate the sum of series 13 + 23 + 33 + 43 + … till n-th term.

Examples:

Input: n = 5
Output: 225
Explanation: 13 + 23 + 33 + 43 + 53 = 225
Input: n = 7
Output: 784
Explanation: 13 + 23 + 33 + 43 + 53 + 63 + 73 = 784"""

                                            #CODE HERE:-

class Solution:
    def sumOfSeries(self,n):
        sm=0
        if(n==0):
            return sm
        else:
            for i in range(n+1):
                sm+=(i)**3
            return sm