"""
# ******************************************************************************

#  Purpose        : To check if the given mathematical expression is balanced or not
#
#  @file          : balanced_parentheses.py
#  @author        : vishnu <vishnu840ranjan@gmail.com>
#  @version       : python 3.5
#  @since         : 17/02/2019

# ******************************************************************************
"""
from Utility.utility_datastructures import Stack


class BalancedParentheses:
    stack = Stack()  # Initialising the stack object
    expression = input("Enter the mathematical expression: ")  # To accept a mathematical expression from the user
    result = False

    for i in range(len(expression)):  # loop over the contents of the stack expression
        char = expression[i]
        #  if it contains open brackets then push
        if char is '(' or char is '[' or char is '{':
            stack.push(char)
        #  if it contains closed brackets then pop and check
        elif char is ')' or char is ']' or char is '}':
            if stack.pop() is not '(':
                break
            elif stack.pop() is not '{':
                break
            elif stack.pop() is not '[':
                break
    if stack.size is 0:  # if the size is equal to zero the expression is balanced
        print("Mathematical expression is balanced")
    else:
        print("Mathematical expression is not balanced")
