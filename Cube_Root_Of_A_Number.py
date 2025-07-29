"""Given a number n, find the cube root of n.

Note: We need to print the floor value of the result.

Examples:

Input: n = 3
Output: 1
Explanation: Cube root of 3 is 1.442 = 1
Input: n = 8
Output: 2
Explanation: Cube root of 8 is 2"""

            #CODE HERE:-

class Solution:
    def cubeRoot(self, n):
        ans=((n)**(1/3))
        if(ans<1):
            return(1)
        else:
            return(int(ans))