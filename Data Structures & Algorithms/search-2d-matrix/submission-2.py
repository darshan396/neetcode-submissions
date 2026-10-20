class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        c = 0
        rl = 0
        rr = len(matrix) - 1
        while rl <= rr:
            rm  = rl + (rr - rl) // 2

            if matrix[rm][0] <= target:
                r = rm
                rl = rm + 1
            else:
                rr = rm - 1
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[r][mid] == target:
                return True
            elif matrix[r][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
            