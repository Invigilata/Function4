def test(*args):
    for arg in args:
        print(arg)

test("Hello", [1, 2, 3], 123)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = 10
result = factorial(n)
print(f"Факториал числа {n} равен {result}")
