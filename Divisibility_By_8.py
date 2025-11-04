"""Given a string representation of a decimal number s, check whether it is divisible by 8.

Example 1:

Input:
s = "16"
Output:
1
Explanation:
The given number is divisible by 8,
so the driver code prints 1 as the output.
Example 2:

Input:
s = "54141111648421214584416464555"
Output:
-1
Explanation:
Given Number is not divisible by 8, 
so the driver code prints -1 as the output."""

                                        #CODE HERE:-

class Solution:
    def DivisibleByEight(self,s):
        n = len(s)
        if n < 3:
            s = int(s)
            if s%8==0:
                return 1
            else:
                return -1
        else:
            m = s[n-3:]
            m = int(m)
            if m == 0:
                return 1
            elif m%8==0:
                return 1
            else:
                return -1