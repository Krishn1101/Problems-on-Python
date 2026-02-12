"""Given a number N.Find the sum of fifth powers of natural numbers till N i.e. 15+25+35+..+N5.

Example 1:

Input:
N=2
Output:
33
Explanation:
The sum is calculated as 15+25=1+32=33.
Example 2:

Input:
N=3
Output:
276
Explanation:
The sum is calculated as 15+25+35
=1+32+243=276."""

                                        #CODE HERE:-

class Solution:
    def sumOfFifthPowers(self,N):
        ans = 0
        for i in range(1,N+1):
            ans+=i**5
        return ans