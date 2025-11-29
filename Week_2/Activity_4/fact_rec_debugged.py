def factorial(n):
    """Calculates n! using recursion."""
    if n < 0:
        raise ValueError("Can't do factorial of a negative number.")
    if n == 0:
        return 1
    # multiply n by factorial of the number before it
    return n * factorial(n - 1)


def fibonacci(n):
    """Gets the n-th Fibonacci number."""
    if n < 0:
        raise ValueError("Can't do fibonacci on negative numbers.")
    if n <= 1:
        return n
    # add the previous two numbers in the sequence
    return fibonacci(n - 1) + fibonacci(n - 2)


def get_positive_int(prompt):
    """Keeps asking until the user types a valid non-negative number."""
    while True:
        s = input(prompt).strip()
        if s == "":
            print("Please type something.")
            continue
        try:
            value = int(s)
        except ValueError:
            print("That's not a number. Try again.")
            continue
        if value < 0:
            print("Number must be zero or higher.")
            continue
        return value


if __name__ == "__main__":
    print("Choose an option:")
    print("1. Factorial")
    print("2. Fibonacci")

    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        # ask user for a number to use in factorial
        n = get_positive_int("Enter a number for factorial: ")
        ans = factorial(n)
    elif choice == "2":
        # ask user for a number for fibonacci
        n = get_positive_int("Enter a number for fibonacci: ")
        ans = fibonacci(n)
    else:
        ans = "Invalid choice"

    print("\nFinal result:", ans)