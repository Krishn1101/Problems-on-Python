"""Given a Numpy array, write a function to perform element-wise exponentiation (raise each element to a power).

Numpy Schema:
You are given a 1-dimensional Numpy array and an integer for the exponent.

Example:
Input:

array = np.array([1, 2, 3, 4])
exponent = 2
Output:

array([ 1,  4,  9, 16])

Explanation: Each element of the array [1, 2, 3, 4] is raised to the power of 2."""

                                                    #CODE HERE:-

def elementwise_exponentiation(arr, exp):
    return arr**exp