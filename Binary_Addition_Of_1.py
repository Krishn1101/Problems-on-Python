"""You are given a binary string s of length n. You have to perform binary addition of the string with '1'.

 

Example 1:

Input: 
n = 4
s = 1010
Output: 1011
Explaination: 
The decimal equivalent of given s is 10, 
Adding 1 gives 11, its binary representation
is 1011.
 

Example 2:

Input: 
n = 3
s = 111
Output: 1000
Explaination: The given number is 7. 
Now 7+1 = 8, whose binary representation 
is 1000."""

                                            #CODE HERE:-

class Solution:
    def binaryAdd(self, n, s):
        n = len(s)
        a = int(s,2)
        a = a+1
        a = bin(a)[2:]
        return(a.rjust(n,'0'))