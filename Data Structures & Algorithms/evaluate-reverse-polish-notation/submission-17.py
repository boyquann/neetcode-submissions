class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in ['*', '+', '-', '/']:
                stack.append(int(t))

            else:
                if len(stack) > 1:
                    operand2 = stack.pop()
                    operand1 = stack.pop()

                    if t == '+':
                        stack.append(operand1 + operand2)

                    elif t == '-':
                        stack.append(operand1 - operand2)
                    
                    elif t == '/':
                        stack.append(int(operand1 / operand2))

                    elif t == '*':
                        stack.append(operand1 * operand2)

        return stack.pop()




        