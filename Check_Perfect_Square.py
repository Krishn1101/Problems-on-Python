"""Given a positive integer n, check if it is perfect square or not.
NOTE: Try to solve the question using only addition and subtraction operation.

Example 1:

Input: n = 35
Output: 0 
Explanation: 35 is not perfect
square because sqrt(35) = 5 but
5*5 !=35.
Example 2:

Input: n = 49
Output: 1
Explanation: sqrt(49) = 7 and 
7*7 = 49, Hence 49 is perfect square."""

                        #CODE HERE:-

class Solution:
    def isPerfectSquare(self, n):
        sqrt_n = int(n**0.5)  # Take the floor of square root
        if sqrt_n * sqrt_n == n:
            return 1
        else:
            return 0
