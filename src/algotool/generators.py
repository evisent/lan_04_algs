"""Генераторы тестовых наборов"""

import random


def _check_size(n):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("size must be int")
    if n < 0:
        raise ValueError("size must be >= 0")


def random_data(n, seed=0):
    _check_size(n)
    rng = random.Random(seed)
    return [rng.randint(-10**6, 10**6) for _ in range(n)]


def sorted_data(n, seed=0):
    _check_size(n)
    rng = random.Random(seed)
    return sorted(rng.randint(-10**6, 10**6) for _ in range(n))


def reversed_data(n, seed=0):
    _check_size(n)
    return sorted_data(n, seed=seed)[::-1]


def nearly_sorted_data(n, seed=0, swaps=3):
    _check_size(n)
    arr = sorted_data(n, seed=seed)
    rng = random.Random(seed)
    for _ in range(swaps):
        if n < 2:
            break
        i = rng.randrange(n)
        j = rng.randrange(n)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def duplicates_data(n, seed=0, distinct=5):
    _check_size(n)
    rng = random.Random(seed)
    pool = [rng.randint(-100, 100) for _ in range(distinct)]
    return [rng.choice(pool) for _ in range(n)]


GENERATORS = {
    "random": random_data,
    "sorted": sorted_data,
    "reversed": reversed_data,
    "nearly": nearly_sorted_data,
    "duplicates": duplicates_data,
}