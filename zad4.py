def make_generator(f):
    def generator():
        n = 1
        while True:
            yield f(n)
            n += 1
    return generator


fibonacci = lambda n: 1 if n <= 2 else fibonacci(n - 1) + fibonacci(n - 2)
catalan = lambda n: 1 if n == 0 else catalan(n - 1) * 2 * (2 * n - 1) // (n + 1)


if __name__ == "__main__":
    fibonacci_gen = make_generator(fibonacci)
    catalan_gen = make_generator(catalan)
    arithmetic_gen = make_generator(lambda n: 2 * n + 1)
    geometric_gen = make_generator(lambda n: 2 ** n)

    print("Fibonacci sequence:")
    for i, val in enumerate(fibonacci_gen(), 1):
        if i > 10:
            break
        print(val)

    print("\nCatalan sequence:")
    for i, val in enumerate(catalan_gen(), 1):
        if i > 10:
            break
        print(val)

    print("\nArithmetic sequence:")
    for i, val in enumerate(arithmetic_gen(), 1):
        if i > 10:
            break
        print(val)

    print("\nGeometric sequence:")
    for i, val in enumerate(geometric_gen(), 1):
        if i > 10:
            break
        print(val)
