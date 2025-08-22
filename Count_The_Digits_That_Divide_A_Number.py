"""Given an integer num, return the number of digits in num that divide num.

An integer val divides nums if nums % val == 0.

 

Example 1:

Input: num = 7
Output: 1
Explanation: 7 divides itself, hence the answer is 1.
Example 2:

Input: num = 121
Output: 2
Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.
Example 3:

Input: num = 1248
Output: 4
Explanation: 1248 is divisible by all of its digits, hence the answer is 4."""

                            #CODE HERE:-
#1.SOLUTION 01:-
class Solution:
    def countDigits(self, num: int) -> int:
        cnt = 0
        s = list(map(int, str(num)))
        for i in s:
            if(num%i==0):
                cnt+=1
        return cnt
    
#            OR

#2. SOLUTION 02:-
class Solution:
    def countDigits(self, num: int) -> int:
        temp = num                       
        ans = 0
        while temp>0:
            r = temp%10                  
            if num%r==0:                 
                ans+=1
            temp = temp//10              
        return ans