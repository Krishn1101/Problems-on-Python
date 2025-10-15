"""Given a single integer N, your task is to find the sum of the square of the first N even natural Numbers.
 

Example 1:

Input: 2
Output: 20
Explanation: 2*(2) + 4*(2) = 20
Example 2: 

Input: 3
Outptut: 56
Explanation: 2*(2) + 4*(2) + 6*(2) = 56"""

                                                #CODE HERE:-

class Solution:
	def sum_of_square_evenNumbers(self, n):
		return (int((2*n*(n+1)*(2*n+1))/3))