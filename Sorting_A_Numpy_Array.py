"""Given a 1-dimensional NumPy array arr, sort its elements in ascending order.

Example:

Input: array = np.array([3, 1, 4, 2])
Output: array([1, 2, 3, 4])
Explanation: The array [3, 1, 4, 2] is sorted in ascending order to [1, 2, 3, 4].
Input: array = np.array([10, 5, 8, 1])
Output: array([1, 5, 8, 10])
Explanation: The array [10, 5, 8, 1] is sorted in ascending order to [1, 5, 8, 10]."""

                                    #CODE HERE:-

class Solution:
    def sortArray(self, arr):
        arr.sort()
        return(arr)