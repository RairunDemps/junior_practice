# doctest_practice.py

def add(a, b):
    """Compute and return the sum of two numbers.

    Usage examples:
    >>> add(4.0, 2.0)
    6.0
    >>> add(4, 2)
    6.0
    >>> add(4.7, 2.3)
    7.0
    """
    return float(a + b)

def greet(name="World"):
    """Print a greeting to the screen.

    Usage examples:
    >>> greet("Pythonista")
    Hello, Pythonista!
    >>> greet()
    Hello, World!
    """
    print(f"Hello, {name}!")
