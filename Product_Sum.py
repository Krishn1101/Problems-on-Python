"""Given two integers a and b. Write a program to find the number of digits in the product of these two integers.

Example 1:

Input: a = 12, b = 4
Output: 2 
Explanation: 12*4 = 48
Hence its a 2 digit number.

Example 2:

Input: a = -24, b = 33
Output: 3
Explanation: -24*33 = -792
Hence its a 3 digit number."""

                                                #CODE HERE:-

class Solution:
    def countDigits (self, a, b):
        ans = a*b
        ans = str(ans)
        if ans[0] == "-":
            ans = ans[1:]
        cnt = len(ans)
        return cnt