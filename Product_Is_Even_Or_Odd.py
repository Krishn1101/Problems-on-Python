"""You are given two long numbers N1 and N2 in a string. You need to find out if the product of these numbers generate an even number or an odd number, If it is an even number print 1 else print 0.

Example 1:

Input: 
N1 = "12"
N2 = "15"
Output: 1
Explanation: 12 * 15 = 180 which is an 
even number.
â€‹Example 2:

Input: 
N1 = "123"
N2 = "457"
Output: 0
Explanation: 123*457 = 56211 which is an 
odd number."""

                                                            #CODE HERE:-

class Solution:
    def EvenOdd(self, n1, n2):
        n1 = int(n1)
        n2 = int(n2)
        ans = n1*n2
        if(ans%2==0):
            return 1
        else:
            return 0