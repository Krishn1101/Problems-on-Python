"""Write a program to calculate nPr . nPr  represents n permutation r and value of nPr  is (n!) / (n-r)!.

Examples:

Input: n = 5, r = 1
Output: 2
Explaination: 5!/(5-2)! = 5!/3! = 120/6 = 20.
Input: n = 6, r = 3
Output: 6
Explaination: 6!/(6-3)! = 6!/3! = 720/6 = 120."""

                                                #CODE HERE:-
                                                
class Solution:
    def nPr(self, n, r):
        import math
        ans=int((math.factorial(n))/(math.factorial(n-r)))
        return ans