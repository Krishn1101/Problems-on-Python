"""You will be given two numbers a and b. Your task is to print 1 if a < b, print 2 if a > b and print 3 if a = b.

Example 1:

Input: 
a = 1234
b = 12345
Output: 1
Explanation: a < b so answer is 1.
Example 2:

Input:
a = 100
b = 1
Output: 2
Explanation: a > b, so answer is 2."""

                                                    #CODE HERE:-

class Solution:
    def check(self, a,b):
        if a<b:
            return(1)
        elif a>b:
            return(2)
        else:
            return(3)