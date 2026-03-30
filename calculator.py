def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exp):
    return base ** exp

if __name__ == "__main__":
    print(add(10, 5))       # 15
    print(subtract(10, 5))  # 5
    print(multiply(10, 5))  # 50
    print(divide(10, 5))    # 2.0
    print(power(2, 8))      # 256
