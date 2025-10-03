"""Given two positive integer n and  k, check if the kth index bit of n is set or not.
 Note: A bit is called set if it is 1. 

Examples : 

Input: n = 4, k = 0
Output: false
Explanation: Binary representation of 4 is 100, in which 0th index bit from LSB is not set. So, return false.
Input: n = 4, k = 2
Output: true
Explanation: Binary representation of 4 is 100, in which 2nd index bit from LSB is set. So, return true.
Input: n = 500, k = 3
Output: false
Explanation: Binary representation of 500 is 111110100, in which 3rd index bit from LSB is not set. So, return false."""

                                            #CODE HERE:-

class Solution:
    def checkKthBit(self, n, k):
        s = bin(n)[2:]
        s = s[::-1]
        if len(s)>k:
            if s[k] == '1':
                return True
        else:
            return False