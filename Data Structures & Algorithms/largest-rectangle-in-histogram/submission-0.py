class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = []  # Stek elementlari: (start_index, height)

        for i, h in enumerate(heights):
            start = i
            # Agar joriy ustun h stekning eng tepasidagi ustundan kalta bo'lsa:
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Kenglik: i - index
                max_area = max(max_area, height * (i - index))
                start = index  # Joriy kalta ustun chapga qarab index-gacha cho'zilishi mumkin
            
            stack.append((start, h))

        # Massiv tugagach, stekda qolgan ustunlar oxirigacha (len(heights)) cho'ziladi
        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))

        return max_area


# Tekshirish:
sol = Solution()
print(sol.largestRectangleArea([7, 1, 7, 2, 2, 4]))  # Chiqish: 8
print(sol.largestRectangleArea([1, 3, 7]))           # Chiqish: 7