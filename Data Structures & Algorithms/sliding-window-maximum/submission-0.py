from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()  # Stores indices of elements
        result = []
        
        for i, num in enumerate(nums):
            # 1. Remove index from front if it falls outside the current window
            if dq and dq[0] < i - k + 1:
                dq.popleft()
                
            # 2. Remove smaller elements from the back (they won't be the max)
            while dq and nums[dq[-1]] <= num:
                dq.pop()
                
            # 3. Add current element's index
            dq.append(i)
            
            # 4. The front of the deque is the max for the current window
            if i >= k - 1:
                result.append(nums[dq[0]])
                
        return result