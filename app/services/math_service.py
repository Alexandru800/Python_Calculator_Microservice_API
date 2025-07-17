from functools import lru_cache

@lru_cache(maxsize=100)
def calculate_factorial(n: int) -> int:
    """Calculate the factorial of a number using recursion with caching."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)