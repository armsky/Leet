"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
Input:	["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
["0","3","/"]
"""

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
                    if a > 0 and b >= 0:
                        stack.append(b / a)
                    elif a = 0:
                        print "not valid"
                    else:
                        stack.append(b / a + 1)
            else:
                stack.append(int(operand))
        return int(stack.pop())

def main():
    solution = Solution()
    #test1 = ["2", "1", "+", "3", "*"]
    #test2 = ["4", "13", "5", "/", "+"]
    #print solution.evalRPN(test1)
    test = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print solution.evalRPN(test)

if __name__ == "__main__":
    main()
