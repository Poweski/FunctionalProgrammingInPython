import functools


def make_generator_mem(f):
    memo = {}

    @functools.wraps(f)
    def memoized(*args):
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]

    return memoized


@make_generator_mem
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print(fib(10))
