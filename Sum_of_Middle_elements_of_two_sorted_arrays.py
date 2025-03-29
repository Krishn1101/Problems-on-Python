"""Given 2 sorted integer arrays arr1 and arr2 of the same size.
Find the sum of the middle elements of two sorted arrays arr1 and arr2."""

"""Examples:

Input: arr1 = [1, 2, 4, 6, 10], arr2 = [4, 5, 6, 9, 12]
Output: 11
Explanation: The merged array looks like [1, 2, 4, 4, 5, 6, 6, 9, 10, 12]. Sum of middle elements is 11 (5 + 6).
Input: arr1 = [1, 12, 15, 26, 38], arr2 = [2, 13, 17, 30, 45]
Output: 32
Explanation: The merged array looks like [1, 2, 12, 13, 15, 17, 26, 30, 38, 45]. Sum of middle elements is 32 (15 + 17)."""

                                       #CODE HERE:-

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        arr1.extend(arr2)
        arr1.sort()
        mid=(0+(len(arr1)))//2
        return (arr1[mid-1]+arr1[mid])