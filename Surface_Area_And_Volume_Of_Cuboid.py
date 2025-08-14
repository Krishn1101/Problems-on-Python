"""Given length l, width b and height h of a cuboid. Your task is to return an array containing the total surface area and volume of the cuboid.

Examples:

Input: l = 1, b = 2, h = 3
Output: 22 6
Explanation: Surface area = 2 * (2 * 3 + 3 * 1 + 1 * 2) = 22 and volume = 1 * 2 * 3 = 6
Input: l = 2, b = 3, h = 5
Output: 62 30
Explanation: Surface area = 2 * (3 * 5 + 5 * 2 + 2 * 3) = 62 and volume = 2 * 3 * 5 = 30"""

                                                            #CODE HERE:-

#User function Template for python3

class Solution:
	def find(self, l, b, h):
	    return(2*(l*b+b*h+h*l),(l*b*h))