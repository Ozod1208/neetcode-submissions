class Solution:

    def calculate(self, a: int, b: int, c: str) -> int:
        match c:
            case "*":
                return a * b
            case "/":
                return int(a / b)
            case "-":
                return a - b
            case _:
                return a + b

    def evalRPN(self, tokens: list[str]) -> int:
        operations: set = {'+', '-', '*', '/'}
        stack: list[str | int] = []

        for token in tokens:
          if token in operations:
            b: int = stack.pop()
            a: int = stack.pop()

            res = self.calculate(a, b, token)
            stack.append(res)
            continue
          stack.append(int(token))
        return stack[0]

sol = Solution()
print(sol.evalRPN(["1","2","+","3","*","4","-"]))

