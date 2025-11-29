class MathSeries:
    def __init__(self, n):
        self.n = n  

    def factorial_recursive(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n in (0, 1):
            return 1
        return n * self.factorial_recursive(n - 1)

    def factorial_series(self):
        series = []
        for i in range(self.n + 1):
            series.append(self.factorial_recursive(i))
        return series

    def fibonacci_recursive(self, n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fibonacci_recursive(n - 1) + self.fibonacci_recursive(n - 2)

    def fibonacci_series(self):
        series = []
        for i in range(self.n + 1):
            series.append(self.fibonacci_recursive(i))
        return series


if __name__ == "__main__":

    obj1 = MathSeries(5)  

    print("Factorial series:", obj1.factorial_series())
    print("Fibonacci series:", obj1.fibonacci_series())
