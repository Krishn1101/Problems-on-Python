"""Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']'. Determine whether the Expression is balanced or not.
An expression is balanced if:

Each opening bracket has a corresponding closing bracket of the same type.
Opening brackets must be closed in the correct order.
Examples :

Input: s = "[{()}]"
Output: true
Explanation: All the brackets are well-formed.
Input: s = "[()()]{}"
Output: true
Explanation: All the brackets are well-formed.
Input: s = "([]"
Output: false
Explanation: The expression is not balanced as there is a missing ')' at the end.
Input: s = "([{]})"
Output: false
Explanation: The expression is not balanced as there is a closing ']' before the closing '}'."""

                                                #CODE HERE:-

class Solution:
    def __init__(self):
        self.stk = []
    def push(self,x):
        self.stk.append(x)
    def pop(self):
        if len(self.stk) == 0:
            return -1
        x = self.stk[-1]
        self.stk.pop()
        return x
    def top(self):
        if len(self.stk) == 0:
            return -1
        return self.stk[-1]
    def size(self):
        return len(self.stk)
    def isBalanced(self, s):
        if s[0] == "}" or s[0] == ")" or s[0] == "]":
            return False
        for i in s:
            if i in "({[":
                self.push(i)
            elif i in ")}]":
                tp = self.top()
                if tp!=-1:
                    if tp == "{" and i == "}" or tp == "[" and i == "]" or tp == "(" and i == ")":
                        self.pop()
                    else:
                        return False
                else:
                    return False
        ans1 = self.top()
        if ans1 == -1:
            return True
        else:
            return False