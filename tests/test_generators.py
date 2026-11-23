import pytest

from algotool.generators import (
    duplicates_data,
    nearly_sorted_data,
    random_data,
    reversed_data,
    sorted_data,
)

GENS = [random_data, sorted_data, reversed_data, nearly_sorted_data, duplicates_data]


def test_reproducible():
    for gen in GENS:
        assert gen(50, seed=123) == gen(50, seed=123)


def test_lengths():
    for gen in GENS:
        assert len(gen(10, seed=1)) == 10
        assert len(gen(0, seed=1)) == 0


def test_sorted_shape():
    a = sorted_data(100, seed=1)
    assert a == sorted(a)
    r = reversed_data(100, seed=1)
    assert r == sorted(r, reverse=True)


def test_nearly_sorted():
    a = nearly_sorted_data(100, seed=1, swaps=2)
    b = sorted_data(100, seed=1)
    diff = sum(1 for x, y in zip(a, b) if x != y)
    assert diff <= 4


def test_duplicates_few_distinct():
    a = duplicates_data(200, seed=1, distinct=3)
    assert len(set(a)) <= 3


def test_wrong_type():
    for gen in GENS:
        with pytest.raises(TypeError):
            gen("10")
        with pytest.raises(ValueError):
            gen(-1)