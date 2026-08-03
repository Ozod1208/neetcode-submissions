class Solution:

  def bs(self, nums: list[int], target: int, left: int, right: int):

    if left > right:
      return -1

    mid = (left + right) // 2

    if nums[mid] == target:
      return mid
    if nums[mid] < target:
      return self.bs(nums, target, mid+1, right)
    elif nums[mid] > target:
      return self.bs(nums, target, left, mid-1)
    pass
  def search(self, nums: list[int], target: int) -> int:
      return self.bs(nums, target, 0, len(nums)-1)

sol = Solution()
print(sol.search([-1,0,2,4,6,8], 4))