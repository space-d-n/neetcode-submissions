class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)

            if c in (')', ']', '}'):
                if not stack:
                    return False
                last = stack.pop()
                if (last, c) not in (
                    ('(', ')'), 
                    ('[', ']'), 
                    ('{', '}')
                ):
                    return False

        if len(stack) == 0:
            return True
        
        return False