"""In this question, we'll use Regex to validate a password. You will be provided a string str which you have to validate.

The validation rules are as follows:

The string is valid only if it starts with lowercase characters, followed by special characters !@#$% followed by numbers.
In any other case the string is not valid.
Example:

Input: 
str = asdsab@!@234
Output: 
True
Explanation: 
The string is valid as characters are
followed by special case characters 
which are then followed by numbers.
Your Task:

This is a function problem. Do not take any input. Complete the function validate() that takes str as input and returns True/False."""

                                                            #CODE HERE:-

def validate(str):
    has_lower = False
    has_special = False
    has_digit = False
    for ch in str:
        if 'a' <= ch <= 'z':
            has_lower = True
        elif ch in "!@#$%":
            has_special = True
        elif '0' <= ch <= '9':
            has_digit = True
    if(has_lower == True and has_special == True and has_digit == True):
        return True
    else:
        return False