import pytest

from algotool.sort import insertion_sort, merge_sort

SORTS = [insertion_sort, merge_sort]


def test_empty():
    for fn in SORTS:
        assert fn([]) == []


def test_single():
    for fn in SORTS:
        assert fn([42]) == [42]


def test_already_sorted():
    for fn in SORTS:
        assert fn([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_reversed():
    for fn in SORTS:
        assert fn([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_duplicates():
    for fn in SORTS:
        assert fn([3, 1, 3, 2, 1, 2]) == [1, 1, 2, 2, 3, 3]


def test_negatives():
    for fn in SORTS:
        assert fn([-3, 0, -10, 5]) == [-10, -3, 0, 5]


def test_input_not_mutated():
    for fn in SORTS:
        src = [3, 1, 2]
        copy = src[:]
        fn(src)
        assert src == copy


def test_wrong_type():
    for fn in SORTS:
        with pytest.raises(TypeError):
            fn("123")
        with pytest.raises(TypeError):
            fn(None)


def test_merge_stable():
    data = [(2, "a"), (1, "b"), (2, "c"), (1, "d")]
    out = merge_sort(data)
    assert [m for _, m in out] == ["b", "d", "a", "c"]