class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for c in s:

            mapping = {'(':')','{':'}','[':']'}
            
            if c in ('(', '{', '['):
                stack.append(c)

            print(stack)

            if c in (')', '}', ']'):
                if len(stack) == 0 or mapping[stack.pop()] != c:
                    return False

        if stack:
            return False
            
        return True