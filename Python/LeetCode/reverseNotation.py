"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
Input:	["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
["0","3","/"]
["4","-2","/","2","-3","-","-"]
"""

#reminder in python, 6/-12 will give you -1 not 0
#int(floatNum) will give you a number near 0, i.e. int(-1.1) = -1, int(-0.9) = 0, int(1.9) = 1

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = [];
        for operand in tokens:
            if operand in ["+","-","*","/"]:
                a = int(stack.pop())
                b = int(stack.pop())
                if operand == '+':
                    stack.append(b + a)
                elif operand == '-':
                    stack.append(b - a)
                elif operand == '*':
                    stack.append(b * a)
                elif operand == '/':
                    stack.append(int(float(b)/a)) 
            else:
                stack.append(int(operand))
        return int(stack.pop())

def main():
    solution = Solution()
    test1 = ["0","3","/"]
    test2 = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]    
    
    print solution.evalRPN(test1)
    test = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print solution.evalRPN(test)
    print solution.evalRPN(test2)

if __name__ == "__main__":
    main()
