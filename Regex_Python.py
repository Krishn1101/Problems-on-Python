"""Regular expressions are extremely helpful in extracting useful information from loads of text. Regular expressions work on pattern-matching techniques. Extracting phone-number, validating passwords, and extracting images from web-pages are but a few examples of regex usage.

In this question, we'll learn the use of Regex in Python. You will be provided a string str in which you have to find all the numbers and print them.

Note: In Python, you need to import re module to use regex

Example:

Input: 
str = asdasd123asmdasdk34234kfdsd34sdfk5
Output: 
123 34234 34 5"""

                                                                    #CODE HERE:-

def numberMatcher(str):
    cnt=0
    ans = ""
    for i in str:
        if(ord(i)>=48 and ord(i)<=57):
            ans+=i
            cnt=0
        else:
            cnt+=1
            if(cnt==1):
                ans+=" "
    print(ans.strip(),end = "")