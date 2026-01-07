"""Given two numbers a and b; you need to perform basic mathematical operation on them. You will be provided an integer named as operator. 
If operator equals to 1 add a and b, then print the result as a string.
If operator equals to 2 subtract b from a, then print the result as a string.
If operator equals to 3 multiply a and b, then print the result as a string.
If operator equals to any another number, print "Invalid Input"(without quotes).
Note: Do not add a new line at the end

Examples:

Input: a = 1, b = 2, opr = 3
Output: 2
Explanation: 1 * 2 = 2
Input: a = 2, b = 2, opr = 2
Output: 0
Explanation: 2 - 2 = 0"""

                                                            #CODE HERE:-

def utility(a, b, opr):
    if opr == 1:
        ans = a + b
        print(str(ans),end="")
    elif opr == 2:
        ans = a - b
        print(str(ans),end="")
    elif opr == 3:
        ans = a * b
        print(str(ans),end="")
    else:
        print("Invalid Input", end="")