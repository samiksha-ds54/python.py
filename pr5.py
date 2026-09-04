# User-defined module
class MyModule:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def square(self, a):
        return a * a


# Create object of user-defined module
m = MyModule()

a = 10
b = 5

print("Addition =", m.add(a, b))
print("Multiplication =", m.multiply(a, b))
print("Square of", a, "=", m.square(a))


# Built-in Python math module
import math

print("\nMathematical Operations")
print("Square root of 25 =", math.sqrt(25))
print("2 raised to power 3 =", math.pow(2, 3))
print("Factorial of 5 =", math.factorial(5))
print("Value of PI =", math.pi)