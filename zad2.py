def forall(pred, iterable):
    if not iterable:
        return True
    return pred(iterable[0]) and forall(pred, iterable[1:])


def exists(pred, iterable):
    if not iterable:
        return False
    return pred(iterable[0]) or exists(pred, iterable[1:])


def at_least(n, pred, iterable):
    if n == 0:
        return True
    if not iterable:
        return False
    if pred(iterable[0]):
        return at_least(n - 1, pred, iterable[1:])
    return at_least(n, pred, iterable[1:])


def at_most(n, pred, iterable):
    if n < 0:
        return False
    if not iterable:
        return True
    if pred(iterable[0]):
        return at_most(n - 1, pred, iterable[1:])
    return at_most(n, pred, iterable[1:])


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    print(forall(lambda x: x % 2 == 0, numbers))
    print(exists(lambda x: x > 3, numbers))
    print(at_least(3, lambda x: x % 2 == 0, numbers))
    print(at_most(2, lambda x: x % 2 == 0, numbers))
