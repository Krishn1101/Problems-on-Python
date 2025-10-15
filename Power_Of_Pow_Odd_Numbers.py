"""Given a single integer N, your task is to find the sum of the square of the first N odd natural Numbers.
 

Example 1:
Input: 2
Output: 10
Explanation: 1**(2) + 3**(2) = 10
Example 2: 
Input: 3
Output: 35
Explanation: 1**(2) + 3**(2) + 5**(2) = 35"""

                                                    #CODE HERE:-


class Solution:
      def sum_of_square_oddNumbers(self, n):
        ans = (n*(2*n+1)*(2*n-1))/3
        return(int(ans))