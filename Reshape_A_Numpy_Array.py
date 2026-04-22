"""Given a Numpy array, write a function to reshape the array into a 2D array with a specified number of rows and columns.

Numpy Schema:
You are given a 1-dimensional Numpy array and need to reshape it to a 2-dimensional array with the given number of rows and columns.

Example:
Input:

array = np.array([1, 2, 3, 4, 5, 6])

rows, cols = 2, 3
Output:

array([[1, 2, 3],
       [4, 5, 6]])

Explanation: The array [1, 2, 3, 4, 5, 6] is reshaped to a 2x3 matrix."""

                                                            #CODE HERE:-

def reshape_array(arr, rows, cols):
    return(arr.reshape(rows,cols))