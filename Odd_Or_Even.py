"""Given a positive integer n, determine whether it is odd or even. Return true if the number is even and false if the number is odd.

Examples:

Input: n = 15
Output: false
Explanation: The number is not divisible by 2, Odd number.
Input: n = 44
Output: true
Explanation: The number is divisible by 2, Even number."""

                                                            #CODE HERE:-

class Solution:
    def isEven (self, n):
        if(n%2==0):
            return True
        else:
            return False