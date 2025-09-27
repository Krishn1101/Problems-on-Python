"""Given a number a, you have to use if, elif, else conditional statements according to the following:
if number is greater than 100: Print "Big" (without quotes)
elif number is smaller than 10: Print "Small" (without quotes)
else: Print "Number" (without quotes)

Examples:

Input: a = 9
Output: Small
Explanation: Here, the else if condition will work as 9 is smaller than 10.
Input: a = 101
Output: Big
Explanation: 101 is greater than 100, so our if statement works and we print Big.
Input: a = 30
Output: Number
Explanation: 30 is neither greater than 100, nor smaller than 10, so the else statement works here."""

                                            #CODE HERE:-

num = int(input())
if num>100:
    print("Big")
elif num<10:
    print("Small")
else:
    print("Number")