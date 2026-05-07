class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        pairs = {
            "{": "}",
            "[": "]",
            "(": ")",
        }

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                elif pairs[stack.pop()] == c:
                    continue
                else:
                    return False

        return True if len(stack) == 0 else False