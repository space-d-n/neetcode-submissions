class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for c in s:

            mapping = {'(':')','{':'}','[':']'}
            
            if c in ('(', '{', '['):
                stack.append(c)

            if c in (')', '}', ']'):
                if not stack or mapping[stack.pop()] != c:
                    return False

        if stack:
            return False

        return True