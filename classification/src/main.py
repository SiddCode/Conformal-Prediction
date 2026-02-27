#!/usr/bin/env python3
"""
Main entry point for your application.

Replace this example code with your actual application logic.
"""

from typing import List


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def sum_numbers(numbers: List[int]) -> int:
    """Return the sum of a list of integers."""
    return sum(numbers)


if __name__ == "__main__":
    # Example usage
    print(greet("World"))
    print(f"Sum of [1, 2, 3, 4, 5] = {sum_numbers([1, 2, 3, 4, 5])}")
