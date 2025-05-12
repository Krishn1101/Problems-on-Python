"""Given two sorted arrays a[] and b[], where each array may contain duplicate elements,
the task is to return the elements in the union of the two arrays in sorted order.

Union of two arrays can be defined as the set containing distinct common elements
that are present in either of the arrays.
Examples:

Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
Output: 1 2 3 4 5 6 7
Explanation: Distinct elements including both the arrays are: 1 2 3 4 5 6 7.
Input: a[] = [2, 2, 3, 4, 5], b[] = [1, 1, 2, 3, 4]
Output: 1 2 3 4 5
Explanation: Distinct elements including both the arrays are: 1 2 3 4 5.
Input: a[] = [1, 1, 1, 1, 1], b[] = [2, 2, 2, 2, 2]
Output: 1 2
Explanation: Distinct elements including both the arrays are: 1 2."""

                                #CODE HERE:-

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        x=set()
        x.update(a)
        x.update(b)
        l=[]
        l.extend(x)
        l.sort()
        return l