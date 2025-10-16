"""Given a decimal number n, return its binary equivalent.

Examples :

Input: n = 12
Output: 1100
Explanation: The binary representation of 12 is "1100", since 12 = 1×2**3 + 1×2**2 + 0×2**1 + 0×2**0
Input: n = 33
Output: 100001
Explanation: The binary representation of 33 is "100001", since 33 = 1×2**5 + 0×2**4 + 0×2**3 + 0×2**2 + 0×2**1 + 1×2**0"""

                                                #CODE HERE:-

class Solution:
    def decToBinary(self, n):
        return(bin(n)[2:])