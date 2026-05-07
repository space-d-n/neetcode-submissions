class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 1:
            return int(tokens[0])
        
        operations = {
            '+': lambda res, x: res + x,
            '-': lambda res, x: res - x,
            '/': lambda res, x: res / x,
            '*': lambda res, x: res * x
        }
        stack = []

        for token in tokens:
            if token not in operations:
                stack.append(token)
            else:
                print(stack)
                b = stack.pop()
                a = stack.pop()

                result = operations[token](int(a), int(b))
                stack.append(result)
                print(stack)

        return int(stack.pop())