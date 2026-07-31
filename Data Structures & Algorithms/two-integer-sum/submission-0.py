class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        low, high = 0, len(nums) - 1

        while low < high:
          need = nums[low] + nums[high]
          if need == target and (nums[low] != target and nums[high] != target):
            return [low,high]
          
          if need < target:
            low += 1
          elif need > target:
            high -= 1
        return []