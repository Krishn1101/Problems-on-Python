"""Given a non-negative integer n, your task is to find the nth Fibonacci number.

The Fibonacci sequence is a sequence where the next term is the sum of the previous two terms. The first two terms of the Fibonacci sequence are 0 followed by 1. The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21

The Fibonacci sequence is defined as follows:

F(0) = 0
F(1) = 1
F(n) = F(n - 1) + F(n - 2) for n > 1
Examples :

Input: n = 5
Output: 5
Explanation: The 5th Fibonacci number is 5.
Input: n = 0
Output: 0 
Explanation: The 0th Fibonacci number is 0.
Input: n = 1
Output: 1
Explanation: The 1st Fibonacci number is 1."""

                                                            #CODE HERE:-


class Solution:
    def nthFibonacci(self, n: int) -> int:
        a=0
        b=1
        c=0
        for i in range(n+1):
            c=a+b
            if(n==0):
                return 0
            elif(n==1):
                return 1
            elif(i==n):
                return c-b
            a=b
            b=c