class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        result = 1

        position_speed = list(zip(position, speed))
        position_speed.sort(key=lambda x: x[0], reverse=True)
        
        print(position_speed)

        times = [0] * len(position_speed)

        for i in range (len(position_speed)):
            times[i] = (target - position_speed[i][0]) / position_speed[i][1]
        
        print(times)

        maximum = times[0]

        for i in range (1, len(position_speed), 1):
            if(times[i] > maximum):
                maximum = times[i]
                result += 1

        return(result)

# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         pair = [(p, s) for p, s in zip(position, speed)]
#         pair.sort(reverse=True)
#         stack = []
#         for p, s in pair:  # Reverse Sorted Order
#             stack.append((target - p) / s)
#             if len(stack) >= 2 and stack[-1] <= stack[-2]:
#                 stack.pop()
#         return len(stack)