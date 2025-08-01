"""Given a number N. The task is to complete the function convertFive() which replaces all zeros in the number with 5 and returns the number.

Example:

Input
2
1004
121

Output
1554
121

Explanation:
Testcase 1:  At index 1 and 2 there is 0 so we replace it with 5.
Testcase 2: There is no,0 so output will remain the same."""

                                                    #CODE HERE:-

class Solution:
    def convertFive(self,n):
        a = str(n)
        a = a.replace("0","5")
        return a