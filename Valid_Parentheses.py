"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false"""

                                                            #CODE HERE:-

class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n%2!=0:
            return False
        st = []
        for i in list(s):
            if i == "(" or i == "{" or i == "[":
                st.append(i)
            else:
                if len(st) == 0:
                    return False
                top = st.pop()
                if i == ")" and top!="(":
                    return False
                elif i == "}" and top!="{":
                    return False
                elif i == "]" and top!="[":
                    return False
        return len(st) == 0