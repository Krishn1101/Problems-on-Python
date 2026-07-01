"""Given a 2D Numpy array arr and a target element, check if a specific element exists in the array return True if it is present; otherwise, return False.

Example:
Input: arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), target = 5
Output: True
Explanation: The element 5 exists in the matrix, so the output is True.

Input: arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), target = 10
Output: False
Explanation: The element 10 does not exists in the matrix, so the output is False."""

                                                            #CODE HERE:-

class Solution:
    def searchElement(self, arr, target):
        for i in range(len(arr)):
            if target in arr[i]:
                return True
        return False