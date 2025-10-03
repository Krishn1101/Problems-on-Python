"""Given an integer n. You have to return the position of the first set bit  from the right side in the binary representation of the number. If there is no set bit in the integer N, then return 0 from the function.  

Examples:

Input: n = 18
Output: 2
Explanation: Binary representation of 18 is 010010,the first set bit from the right side is at position 2.
Input: n = 12
Output: 3 
Explanation: Binary representation of  12 is 1100, the first set bit from the right side is at position 3.
Input: n = 1
Output: 1
Explanation: Binary representation of  1 is 1, the first set bit from the right side is at position 1."""

                                                            #CODE HERE:-

class Solution:
    def getFirstSetBit(self,n):
        s = bin(n)[2:]
        s = s[::-1]
        for i in range(len(s)):
            if s[i] == '1':
                return i+1