def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def validate_name(name):
    if not name.strip():
        raise ValueError("Name cannot be empty")
    return name.strip()
