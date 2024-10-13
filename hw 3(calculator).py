class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self):
        return self.num1 + self.num2

    def __sub__(self):
        return self.num1 - self.num2

    def __mul__(self):
        return self.num1 * self.num2

    def __truediv__(self):
        if self.num2 == 0:
            raise ZeroDivisionError
        return self.num1 / self.num2

calculator = Calculator(20, 5)
print(calculator.num1 - calculator.num2)
print(calculator.num1 / calculator.num2)
print(calculator.num1 * calculator.num2)
print(calculator.num1 + calculator.num2)