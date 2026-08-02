class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []

        brackets: dict[str, str] = {
          "}": "{",
          "]": "[",
          ")": "("
        }

        for char in s:
          if char in brackets:
                # If stack is empty OR top of stack doesn't match
                if not stack or stack.pop() != brackets[char]:
                    return False
          else:
              stack.append(char)
        return len(stack) == 0

sol = Solution()
print(sol.isValid("([{}])"))