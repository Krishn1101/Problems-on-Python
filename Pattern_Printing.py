"""Given a number N. The task is to print a series of asterisk(*) from 1 till N terms with increasing order and difference being 1.

Example 1:

Input:
N = 3
Output:
* ** ***
Explanation:
First, print 1 asterisk then space after
that print 2 asterisk and space after that 
print 3 asterisk now stop as N is 3.
Example 2:

Input:
N = 5
Output:
* ** *** **** ***** 
Explanation:
First, print 1 asterisk then space after
that print 2 asterisk and space and do this
3 more times."""

                                                            #CODE HERE:-

class Solution:
    def printPattern(self, N):
        for i in range(1,N+1):
            print("*" * i,end = " ")