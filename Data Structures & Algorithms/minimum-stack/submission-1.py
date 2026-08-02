class MinStack:

    def __init__(self):
      self.array: list[int] = []
      self.reverse_array: list = []

    def push(self, val: int) -> None:
        self.array.append(val)
        current_min = min(val, self.reverse_array[-1]) if self.reverse_array else val
        self.reverse_array.append(current_min)

    def pop(self) -> None:
        self.array.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.reverse_array[-1]
