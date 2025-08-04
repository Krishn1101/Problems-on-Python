"""Given three integers p, r and t, denoting Principal, Rate of Interest and Time period respectively. Your task is to calculate Simple Interest.

Examples:

Input: p = 100, r = 20, t = 2
Output: 40.00
Explanation: The simple interest on 100 at a rate of 20% across 2 time periods is 40.
Input: p = 999, r = 9, t = 9
Output: 809.19
Explanation: The simple interest on 999 at a rate of 9% across 9 time periods is 809.19"""

                                                            #CODE HERE:-

class Solution:
    def simpleInterest(self,A,B,C):
        return((A*B*C)/100)