"""Given a non-negative integer n. You have to check if it is a power of 2 or not. 

Examples

Input: n = 8
Output: true
Explanation: 8 is equal to 2 raised to 3 (23 = 8).
Input: n = 98
Output: false
Explanation: 98 cannot be obtained by any power of 2.
Input: n = 1
Output: true
Explanation: (20 = 1)."""

                                    #CODE HERE:-

class Solution:
    def isPowerofTwo(self, n):
        #Method 1:-

        # if(n>0 and (n&(n-1))==0):
        #     return True
        # else:
        #     return False

        #Method 2:-
        if(n<=0):
            return False
            
        while(n%2==0):
            n=n//2
        return n == 1