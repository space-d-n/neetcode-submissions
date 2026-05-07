class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix) * len(matrix[-1]) - 1

        m = len(matrix)
        n = len(matrix[0])

        while l <= r:

            mid = (r + l) // 2

            mm = mid // n
            nm = mid % n

            if (matrix[mm][nm] == target):
                return True
            elif (matrix[mm][nm] < target):
                l = mid + 1
            elif (matrix[mm][nm] > target):
                r = mid - 1

        return False
