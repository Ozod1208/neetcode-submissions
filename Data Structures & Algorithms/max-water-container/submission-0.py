class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left, right, max_water = 0, len(heights) - 1, 0

        while left < right:
          current_water = (right - left) * min(heights[left], heights[right])

          max_water = max(max_water, current_water)

          if heights[left] < heights[right]:
              left += 1
          else:
              right -= 1
        return max_water