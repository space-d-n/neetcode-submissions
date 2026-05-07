class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 1:
            return int(tokens[0])
        
        operations = {
            '+': lambda res, x: res + x,
            '-': lambda res, x: res - x,
            '/': lambda res, x: int(res / x),
            '*': lambda res, x: res * x
        }
        stack = []

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                result = operations[token](a, b)
                stack.append(result)

        return stack.pop()