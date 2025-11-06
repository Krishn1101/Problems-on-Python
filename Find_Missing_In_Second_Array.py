"""Given two integer arrays a and b, the task is to find the numbers which are present in the first array a, but not present in the second array b.

Note: Numbers to be returned should in order as they appear in array a.

Examples :

Input: a[] = [1, 2, 3, 4, 5, 10], b[] = [2, 3, 1, 0, 5]
Output: [4, 10]
Explanation: 4 and 10 are present in first array, but not in second array.
Input: a[] = [4, 3, 5, 9, 11], b[] = [4, 9, 3, 11, 10]
Output: [5]  
Explanation: Second array does not contain element 5.
Input: a[] = [9], b[] = [7, 9, 4, 9, 9, 9]
Output: []"""

                                                            #CODE HERE:-

class Solution:
    def findMissing(self,a,b):
        b_set = set(b)
        arr = []
        for i in a:
            if i not in b_set:
                arr.append(i)
        return arr