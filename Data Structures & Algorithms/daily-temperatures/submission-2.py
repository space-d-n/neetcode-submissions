class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [(temperatures[-1], len(temperatures) - 1)]
        result = [0] * len(temperatures)

        for i in range(len(temperatures) - 2, -1, -1):

            while stack:
                if temperatures[i] >= stack[-1][0]:
                    stack.pop()
                else:
                    break

            if stack:
                result[i] = stack[-1][1] - i
            else:
                result[i] = 0

            stack.append((temperatures[i], i))

        return result