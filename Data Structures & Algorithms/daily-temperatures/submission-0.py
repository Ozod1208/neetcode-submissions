class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # Indekslarni saqlaydi

        for i, temp in enumerate(temperatures):
            # Agar bugungi harorat stack tepasidagi kun haroratidan issiq bo'lsa
            while stack and temp > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx  # Kunlar farqini yozamiz
            
            stack.append(i)  # Bugungi kun indeksini stackga qo'shamiz

        return res