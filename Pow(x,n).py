"""Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25"""

                            #CODE HERE:-
#Method 01:-
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return (x**n)
#Method 02:-
        if(n%2==0):
            return (x**(n//2))**2
        else:
            return ((x**(n//2))**2) * x
#Method 03:-        ye code ki time complexity kam hogi O(log n) kyu ki hum yaha har step m n//2 karte jaa rahe hai...
    def findPow(self, x, n):
        #Base case:
        if n==0:
            return 1
        #Recursive case:
        a = self.findPow(x,n//2)
        if n%2==0:
            return a*a
        else:
            return a*a*x
    def myPow(self, x: float, n: int):
        if n>=0:
            return self.findPow(x,n)
        else:
            return (1/self.findPow(x,n*(-1)))