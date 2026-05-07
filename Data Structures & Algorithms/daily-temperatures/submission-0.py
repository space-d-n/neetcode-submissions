class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [(temperatures[-1], len(temperatures) - 1)]
        result = [0]

        for i in range(len(temperatures) - 2, -1, -1):

            print(temperatures[i])
            print(stack)
            print(result)
            print()

            while stack:
                if temperatures[i] >= stack[-1][0]:
                    stack.pop()
                else:
                    break

            if stack:
                result.append(stack[-1][1] - i)
            else:
                result.append(0)

            stack.append((temperatures[i], i))

        return result[::-1]