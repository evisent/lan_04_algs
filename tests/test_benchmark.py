from algotool.benchmark import bench_fib, bench_sort
from algotool.generators import GENERATORS


def test_bench_fib_markdown():
    lines = bench_fib(sizes=(100, 1000))
    assert len(lines) >= 3
    assert lines[0].startswith("|")
    assert "100" in lines[2]


def test_bench_sort_markdown():
    subset = {"random": GENERATORS["random"], "sorted": GENERATORS["sorted"]}
    lines = bench_sort(subset, sizes=(50, 200))
    assert len(lines) == 2 + 4
    assert all(line.startswith("|") for line in lines)
    