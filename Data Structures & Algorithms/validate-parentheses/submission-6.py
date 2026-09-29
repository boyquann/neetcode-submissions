class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        stack = []

        for ch in s:
            if ch in match.values():
                stack.append(ch)

            elif ch in match.keys():
                if len(stack) == 0:
                    return False
                    
                if match[ch] != stack.pop():
                    return False

        return len(stack) == 0



        