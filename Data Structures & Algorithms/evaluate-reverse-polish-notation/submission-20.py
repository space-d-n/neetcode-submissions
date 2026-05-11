class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ops = {
            "+" : lambda x,y: x+y,
            "-" : lambda x,y: x-y,
            "*" : lambda x,y: x*y,
            "/" : lambda x,y: x/y
        }
        stack = []

        for token in tokens:

            print(token)
            if token not in (ops.keys()):
                stack.append(token)
                continue
            print(stack)
            print("operating")

            op2 = int(stack.pop())
            op1 = int(stack.pop())
            result = ops[token](op1, op2)
            stack.append(result)
            print(f"result {result}")

        return int(stack.pop())

