class Calculator:

    def __init__(self, initial_value=0):
        self.result = initial_value
        
    def add(self, value):
        self.result += value
        return self.result

    def sub(self, value):
        self.result -= value
        return self.result

    def mult(self, value):
        self.result *= value
        return self.result

    def div(self, value):
        self.result /= value
        return self.result

    def reset(self):
        self.result = 0
        return self.result

calc = Calculator(4)
calc2 = Calculator(5)

calc.add(3)
print (calc.result)

#devient

print(calc.add(3))