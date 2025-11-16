"""Given two integers m and n , return the position (1-based from the right) of the rightmost bit where they differ in binary, or -1 if both are identical.

Examples: 

Input: m = 11, n = 9
Output: 2
Explanation: Binary representation of the given numbers are: 1011 and 1001, 2nd bit from right is different.
Input: m = 52, n = 4
Output: 5
Explanation: Binary representation of the given numbers are: 110100 and 0100, 5th-bit from right is different.
Input: m = 29, n = 15
Output: 2
Explanation: Binary representation of the given numbers are: 29 in binary is 11101, 15 in binary is 01111. The 2nd bit from the right is different."""

                                                            #CODE HERE:-

class Solution:
    def posOfRightMostDiffBit(self,m,n):
        if m == n:
            return -1
        s1 = bin(m)[2:]
        s2 = bin(n)[2:]
        s1 = s1.zfill(4)
        s2 = s2.zfill(4)
        s1 = s1[::-1]
        s2 = s2[::-1]
        len_s1 = len(s1)
        len_s2 = len(s2)
        b = True
        i = 0
        while(b==True):
            if i==len_s1 or i==len_s2:
                return i+1
            else:
                if s1[i]!=s2[i]:
                    b=False
                    return i+1
                else:
                    i+=1
        return -1