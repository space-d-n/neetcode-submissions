class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_volume = 0

        for i in range(len(heights)):
            
            j = i + 1

            while j < len(heights):
                volume = (j - i) * min(heights[j], heights[i])

                if volume > max_volume:
                    max_volume = volume
                
                j += 1

        return max_volume

            