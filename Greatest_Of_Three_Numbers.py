"""Given 3 numbers a, b and c. Find the greatest number among them.

Examples:

Input: a = 10, b = 3, c = 2
Output: 10
Explanation: 10 is greatest among the three 
Input: a = -4, b = -3, c = -2
Output: -2
Explanation: -2 is greatest among the three"""

                #CODE HERE:-

class Solution:
    def greatestOfThree(self, a, b, c):
        return(max(a,b,c))