"""Given a positive integer N, find the last digit of the Nth term from the Fibonacci series.

Note: For N=0 you have to return 0.
 

Example 1:

Input:
N = 5
Output:
5
Explanation:
5th Fibonacci number is 5
Example 2:

Input:
N = 14
Output:
7
Explanation:
14th Fibonacci number is 377
It's last digit is 7"""

                                        #CODE HERE:-

class Solution:
    def fib (self,N):
        if N == 0 or N == 1:
            return N
        else:
            a,b = 0,1
            for i in range(2,N+1):
                a,b = b,a+b
            ans = str(b)
            return(ans[-1])