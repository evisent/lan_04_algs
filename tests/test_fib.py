import sys

import pytest

from algotool.fib import fib_iterative, fib_recursive

FNS = [fib_iterative, fib_recursive]


def test_known_values():
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for n, want in enumerate(expected):
        assert fib_iterative(n) == want
        assert fib_recursive(n) == want


def test_large():
    assert fib_iterative(100) == 354_224_848_179_261_915_075


def test_negative():
    for fn in FNS:
        with pytest.raises(ValueError):
            fn(-1)


def test_wrong_type():
    for fn in FNS:
        for bad in (1.0, "5", None, [1], True):
            with pytest.raises(TypeError):
                fn(bad)


def test_recursion_limit():
    with pytest.raises(RecursionError):
        fib_recursive(sys.getrecursionlimit() + 10)