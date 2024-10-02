class Calculation:
    def __init__(self, operation: str, a: float, b: float):
        self.operation = operation
        self.a = a
        self.b = b

    def execute(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            if self.b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return self.a / self.b
