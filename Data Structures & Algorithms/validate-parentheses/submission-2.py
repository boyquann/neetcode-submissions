class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')' : '(',
                    '}' : '{',
                    ']' : '['}

        stack = []

        for ch in s:
            if ch in brackets.values():
                stack.append(ch)

            elif ch in brackets.keys():
                if len(stack) == 0:
                    return False

                if stack.pop() != brackets[ch]:
                    return False

        return len(stack) == 0

        