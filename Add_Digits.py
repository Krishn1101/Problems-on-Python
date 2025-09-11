"""Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0"""

                                                #CODE HERE:-

class Solution:
    def addDigits(self, num: int) -> int:
        ans = list(str(num))
        sm,final_ans = 0,0
        if len(ans)==1:
            final_ans = ans[0]
            return(int(final_ans))
        else:
            for i in range(len(ans)):
                sm+=int(ans[i])
            return self.addDigits(sm)