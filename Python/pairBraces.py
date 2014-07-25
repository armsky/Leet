expressions = ["}[]{}", "{}[]()", "{[()()]}", "{[()]}{}", "{([})}]","[][{(])}"]

for expression in expressions:
    pair = True
    stack = []
    pushChars, popChars = "([{", ")]}"
    for char in expression:
        if char in pushChars:
            stack.append(char)
        elif char in popChars:
            if not len(stack):
                pair = False
                break
            else:
                stackTop = stack.pop()
                pairedBrace = pushChars[popChars.index(char)]
                if stackTop != pairedBrace:
                    pair = False
                    break
        #if char == expression[len(expression)-1]:
    if pair:
        print 1
    else:
        print 0
