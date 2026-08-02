class MinStack:

    def __init__(self):
        self.stack: list[int] = []
        self.min_stack: list[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Agar min_stack bo'sh bo'lsa val o'zi min, aks holda yangi val bilan oldingi min taqqoslanadi
        current_min = min(val, self.min_stack[-1]) if self.min_stack else val
        self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]