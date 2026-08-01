class Solution:
    def trap(self, heights: list[int]) -> int:

        if not heights:
            return 0
        
        left, right = 0, len(heights) - 1
        left_max, right_max = heights[left], heights[right]
        points = 0

        while left < right:
            # Chap devor o'ng devordan pastroq bo'lsa
            if left_max < right_max:
                left += 1
                # Rekordni yangilaymiz
                left_max = max(left_max, heights[left])
                # Chuqurlik bo'lsa, suv qo'shiladi (aks holda 0 qo'shiladi)
                points += left_max - heights[left]
            else:
                right -= 1
                # Rekordni yangilaymiz
                right_max = max(right_max, heights[right])
                # Chuqurlik bo'lsa, suv qo'shiladi (aks holda 0 qo'shiladi)
                points += right_max - heights[right]

        return points