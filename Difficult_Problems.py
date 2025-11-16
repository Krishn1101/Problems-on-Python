"""Given a Number N in String form, Print 1 If the digits of the number are in non-decreasing or non-increasing order, else print 0.

 

Example 1:

Input:
N = "1233"
Output:
1
Explanation:
The digits of the number are in non-
decreasing order. So, the Output is 1.
Example 2:

Input:
N = "1263"
Output:
0
Explanation:
The digits of the number are neither in
non-decreasing nor in non-increasing order.
So, the Output is 0."""

                                                            #CODE HERE:-

class Solution:
    def difProblem(self, N):
        asc = list(N)
        asc.sort()
        desc = list(N)
        desc.sort(reverse = True)
        if "".join(asc) == N or "".join(desc) == N:
            return 1
        else:
            return 0