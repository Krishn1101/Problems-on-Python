"""Given two arrays arr1[] and arr2[], return the merged array in ascending order containing unique elements.

Examples:

Input: arr1[] = [11, 1, 8], arr2[] = [10, 11]
Output: [1, 8, 10, 11]
Explanation: The ouput array after merging both the arrays and removing duplicates is [1, 8, 10, 11]
Input: arr1[] = [7, 1, 5, 3, 9], arr2[]  = [8, 4, 3, 5, 2, 6]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]"""

                                            #CODE HERE:-

class Solution:
    def mergeNsort(self, arr1, arr2):
        arr1.extend(arr2)
        arr1 = list(set(arr1))
        arr1.sort()
        return arr1