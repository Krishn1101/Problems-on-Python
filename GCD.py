"""Given two numbers A and B. The task is to find the GCD of  A and B.
The GCD of two numbers is the largest number that can divide both A and B perfectly.

Examples:

Input: A = 6, B = 9
Output: 3
Explanation: After 3 there is no number that can divide both 6 and 9 perfectly.
Input: A = 10, B = 15
Output: 5
Explanation: 5 is the greatest common divisor of 10 and 15."""

                                    #CODE HERE:-

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b,a%b)