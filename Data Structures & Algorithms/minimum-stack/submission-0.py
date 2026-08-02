class MinStack:

    def __init__(self):
      self.array: list[int] = []

    def push(self, val: int) -> None:
        self.array.append(val)

    def pop(self) -> None:
        self.array.pop()

    def top(self) -> int:
        return max(self.array)

    def getMin(self) -> int:
        return min(self.array)
