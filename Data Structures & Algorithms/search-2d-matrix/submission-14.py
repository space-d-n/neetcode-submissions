class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix) * len(matrix[-1]) - 1

        m = len(matrix)
        n = len(matrix[0])

        print(f"{l}-{r} , {m}-{n}")

        while l <= r:

            ml = l // n
            nl = l % n

            mr = r // n
            nr = r % n

            mid = (r + l) // 2

            mm = mid // n
            nm = mid % n

            

            print("_")
            print(f"{ml}-{nl} : {mm}-{nm} : {mr}-{nr}")
            print(f"{l}-{mid}-{r}")

            if (matrix[mm][nm] == target):
                print('_')
                return True
            elif (matrix[mm][nm] < target):
                l = mid + 1
                print('_._')
            elif (matrix[mm][nm] > target):
                r = mid - 1
                print('._.')

        return False
