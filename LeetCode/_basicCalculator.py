"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.
"""
def calculate(s):
    s.replace(" ", "")
    signs = [1,1]
    result = 0
    temp = ""
    for char in s:
        if char.isdigit():
            temp += char
        elif char != " ":
            if temp.isdigit():
                result = result + signs[-1] * int(temp)
                temp = ""
            if char == "-":
                signs.append(signs[-1] * -1)
            elif char == "+":
                signs.append(signs[-1] * 1)
            elif char == ")":
                signs.pop()
        print temp
        print result
        print signs
        print
    if temp != "":
        result = result + signs[-1] * int(temp)
    return result

print calculate(" 2-1 + 2 ")

