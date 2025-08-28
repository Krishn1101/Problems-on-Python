"""Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33
Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.
Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1)."""

                                    #CODE HERE:-

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #Method 1:-
        if(n<=0):
            return False
        while(n%3==0):
            n=n//3
        return n == 1

        #Method 2:-
        if n<=0:
            return False
        if n==1:
            return True
        if n%3!=0:
            return False
        return self.isPowerOfThree(n//3)