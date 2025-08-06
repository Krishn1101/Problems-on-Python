"""Given a number N in the form of string, the task is to check if the number is divisible by 5. 

 

Example 1:

Input:
N = "5"
Output:
1
Explanation:
5 is divisible by 5.
 

Example 2:

Input:
N = "1000001"
Output:
0
Explanation:
1000001 is not divisible 
by 5."""

                                        #CODE HERE:-

class Solution:
    def divisibleBy5 (ob,N):
        if((N[len(N)-1]=="0") or (N[len(N)-1]=="5")):
            return 1
        else:
            return 0