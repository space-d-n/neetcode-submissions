class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            days = 0
            while stack:
                if temperatures[i] >= stack[-1][0]:
                    stack.pop()
                else:
                    result[i] = stack[-1][1] - i
                    break
                
            stack.append((temperatures[i], i))
        
        return result

            