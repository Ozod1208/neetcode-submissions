class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])

        def helper(left: int, right: int) -> bool:
            # 1. Bazaviy to'xtash sharti: qidiruv sohasi tugadi
            if left > right:
                return False
            
            mid = (left + right) // 2
            
            # 1D indeksni 2D matritsa indekslariga o'giramiz
            row = mid // n
            col = mid % n
            val = matrix[row][col]
            
            # 2. Rekursiv shartlar
            if val == target:
                return True
            elif val < target:
                # O'ng yarmini rekursiv qidiramiz
                return helper(mid + 1, right)
            else:
                # Chap yarmini rekursiv qidiramiz
                return helper(left, mid - 1)

        # Qidiruvni 0-indeksdan (m * n - 1) indeksgacha boshlaymiz
        return helper(0, m * n - 1)
