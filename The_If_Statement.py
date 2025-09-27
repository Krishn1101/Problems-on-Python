"""You are given a number n, you have to use the if statement to print "Big" (without quotes) if the given number is greater than 100. The statement "Number" (without quotes) will be printed regardless.

Note: Follow Sample cases for the output format. After printing move the cursor to the next line.

Examples :

Input: n = 10
Output: 
Number
Explanation: 10 is less than 100, so we don't print Big and Number will be printed by default.
Input: n = 101
Output:
Big
Number
Explanation: 101 is greater than 100, so we print Big and Number will be printed by default in the next line."""

                                                        #CODE HERE:-

n = int(input())
if n>100:
    print("Big")
print("Number")