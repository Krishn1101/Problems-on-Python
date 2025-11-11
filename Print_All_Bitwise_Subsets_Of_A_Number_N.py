"""Given a number N, print all the numbers which are a bitwise subset of the binary representation of N. Bitwise subset of a number N will be the numbers i in the range 0 ≤ i ≤ N which satisfy the below condition:
N & i == i

Example 1:

Input:
N = 5
Output: 5 4 1 0
Explanation:
   0 & 5 = 0
   1 & 5 = 1
   2 & 5 = 0
   3 & 5 = 1
   4 & 5 = 4
   5 & 5 = 5
  
Example 2:

Input:
N = 9
Output: 9 8 1 0"""

                                                            #CODE HERE:-

class Solution:
    def printSubsets(self, N):
        arr = []
        for i in range(N+1):
            if i&N==i:
                arr.append(i)
                arr.sort(reverse = True)
        return arr