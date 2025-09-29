"""Given an integer n. Write a program to print all the divisors of n in a single line.

Examples:

Input: n = 12
Output: 1 2 3 4 6 12
Explanation: 12 is divisible by 1 2 3 4 6 12.
Input: n = 10
Output: 1 2 5 10
Explanation: 10 is divisible by 1 2 5 10."""

                                        #CODE HERE:-

class Solution:
    def print_divisors(self, n):
        for i in range(1,n+1):
            if n%i==0:
                print(i, end = " ")