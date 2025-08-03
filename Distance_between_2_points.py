"""Given coordinates of 2 points on a cartesian plane, find the distance between them rounded up to nearest integer.

Example 1:

Input: 0 0 2 -2
Output: 3
Explanation: Distance between (0, 0) 
and (2, -2) is 3.
Example 2:

Input: -20 23 -15 68
Output: 45
Explanation: Distance between (-20, 23) 
and (-15, 68) is 45."""

                                                    #CODE HERE:-

class Solution:
	def distance(self, x1, y1, x2, y2):
		import math
		a = (x2-x1)**2
		b = (y2-y1)**2
		return(round(math.sqrt(a+b)))