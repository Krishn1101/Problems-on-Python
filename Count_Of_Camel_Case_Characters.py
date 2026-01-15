"""Given a string. Count the number of Camel Case characters in it.

Example 1:

Input:
S = "ckjkUUYII"
Output: 5
Explanation: Camel Case characters present:
U, U, Y, I and I.

â€‹Example 2:

Input: 
S = "abcd"
Output: 0
Explanation: No Camel Case character
present
."""

                            #CODE HERE:-

class Solution:
    def countCamelCase (self,s):
        cnt = 0
        for i in s:
            if 65<=ord(i)<=90:
                cnt+=1
        return cnt