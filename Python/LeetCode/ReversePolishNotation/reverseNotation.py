"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = [];
        for operand in tokens:
            if operand:
                if operand == '+':
                    stack.append(int(stack.pop()) + int(stack.pop()))
                elif operand == '-':
                    stack.append(int(-1 * stack.pop()) + int(stack.pop()))
                elif operand == '*':
                    stack.append(int(stack.pop()) * int(stack.pop()))
                elif operand == '/':
                    stack.append(int(float(1 / float(stack.pop())) * int(stack.pop())))
                else:
                    stack.append(int(operand))
        return int(stack.pop())

def main():
    solution = Solution()
    test1 = ["2", "1", "+", "3", "*"]
    test2 = ["4", "13", "5", "/", "+"]
    print solution.evalRPN(test1)
    print solution.evalRPN(test2)

if __name__ == "__main__":
    main()
