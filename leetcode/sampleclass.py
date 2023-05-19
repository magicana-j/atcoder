class Sample:
    def __init__(self):
        self.a = 0
        self.b = 0

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def sum(self) -> int:
        return self.a + self.b

    def set(self, a: int, b: int) -> int:
        self.a = a
        self.b = b


my_sum = Sample(1, 2)
print(my_sum.sum())
