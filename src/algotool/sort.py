"""Сортировки: insertion (квадратичная) и merge (эффективная)"""


def _check(seq):
    if not isinstance(seq, (list, tuple)):
        raise TypeError(f"expected list or tuple, got {type(seq).__name__}")


def insertion_sort(seq):
    _check(seq)
    arr = list(seq)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(seq):
    _check(seq)
    arr = list(seq)

    def _merge(left, right):
        out = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                out.append(left[i])
                i += 1
            else:
                out.append(right[j])
                j += 1
        out.extend(left[i:])
        out.extend(right[j:])
        return out

    def _sort(a):
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        return _merge(_sort(a[:mid]), _sort(a[mid:]))

    return _sort(arr)