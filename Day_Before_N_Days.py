"""Given two integers d and n. Where d is the day, out of 7 days of the week, d varies from 0 to 6 as shown below.
0 - Sunday
1 - Monday
2 - Tuesday
3 - Wednesday
4 - Thursday
5 - Friday
6 - Saturday

You have to return the index for the day which is n days before the given day d.

Examples:

Input: d = 4, n = 3
Output: 1
Explanation: 3 days before the 4th(Thursday) is 1(Monday).
Input: d = 2, n = 19
Output: 4
Explanation: 19 days before the 2nd(Tuesday) is 4(Thursday)."""

                                                        #CODE HERE:-

class Solution:
    def findAnswer(self, d, n):
        import math
        arr = [0,1,2,3,4,5,6]
        add = math.ceil(n/6)
        for i in range(add):
            arr.extend([0,1,2,3,4,5,6])
        fin_ans = d - n
        return arr[fin_ans]