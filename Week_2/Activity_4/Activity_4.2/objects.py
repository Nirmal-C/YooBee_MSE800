class MathSeries:

    @staticmethod
    def factorial_recursive(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n in (0, 1):
            return 1
        return n * MathSeries.factorial_recursive(n - 1)

    @staticmethod
    def factorial_series(n):
        series = []
        for i in range(n + 1):
            series.append(MathSeries.factorial_recursive(i))
        return series

    @staticmethod
    def fibonacci_recursive(n):
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        if n == 0:
            return 0
        if n == 1:
            return 1
        return MathSeries.fibonacci_recursive(n - 1) + MathSeries.fibonacci_recursive(n - 2)

    @staticmethod
    def fibonacci_series(n):
        series = []
        for i in range(n + 1):
            series.append(MathSeries.fibonacci_recursive(i))
        return series


if __name__ == "__main__":
    n = 5

    print("Factorial series:", MathSeries.factorial_series(n))
    print("Fibonacci series:", MathSeries.fibonacci_series(n))
