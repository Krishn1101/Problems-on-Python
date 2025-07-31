"""You are given a mean M, and an integer D. The mean M is the mean of 3 numbers A, B, and C. Find the mean of A, B, C, and D.
Note : Mean is floor of the average of the given numbers and is calculated by dividing the sum of given numbers by the total number of numbers. 

Example:

Input:
D = 5
M = 3
Output:
3
Explanation:
Mean of 3 numbers is 3. If we include 5 and find the new mean, it will be 3.

Input:
D = 13
M = 9
Output:
10
Explanation:
Mean of 3 numbers is 9. If we include 13 and find the new mean, it will be (9+9+9+13)/4 = 10.
Your Task:
This is a function problem. You do not need to take any input. Complete the function mean() and return the new mean."""

                                                    #CODE HERE:-

def mean(D,M):
    M = (3*M+D)//4
    return M