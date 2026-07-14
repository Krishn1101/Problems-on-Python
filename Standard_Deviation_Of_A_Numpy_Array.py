"""Given a 1-dimensional NumPy array arr of size n, find the standard deviation of all elements present in the array. The standard deviation measures the amount of variation or dispersion of the elements from their mean.

Examples:
Input: arr = np.array([1, 2, 3, 4, 5])
Output: 1.4142135623730951
Explanation: The standard deviation of the elements in the array [1, 2, 3, 4, 5] is approximately 1.4142135623730951.
Input: arr = np.array([2, 2, 2, 2])
Output: 0.0
Explanation: All elements are equal, so the standard deviation is 0.0."""

                                                            #CODE HERE:-

class Solution:
    def arrayStd(self, arr):
        mean = sum(arr)/len(arr)
        sq = 0
        for i in arr:
            sq+=(i - mean)**2
        return((sq/len(arr))**0.5)