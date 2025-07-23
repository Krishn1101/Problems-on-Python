"""Given an integer n, your task is to compute the sum of all natural numbers from 1 to n (inclusive). If n is 0, the sum should be 0.

Examples:

Input: n = 6
Output: 21
Explanation: The sum of natural numbers up to 6 is: 1 + 2 + 3 + 4 + 5 + 6 = 21
Input: n = 4
Output: 10
Explanation: The sum of natural numbers up to 4 is: 1 + 2 + 3 + 4 = 10
Input: n = 0
Output: 0
Explanation: Since n is 0, the sum is 0."""

                                                        #CODE HERE:-

#User function Template for python3

class Solution:
    def sumOfNaturals(self, n):
        sm=0
        if(n==0):
            return sm
        else:
            for i in range(n+1):
                sm+=i
            return sm