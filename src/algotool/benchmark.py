import time

from .fib import fib_iterative, fib_recursive
from .sort import insertion_sort, merge_sort

REPEATS = 5
LIMIT_QUADRATIC = 10_000  
LIMIT_RECURSIVE = 30      

def _timeit(fn, data):
    best = float("inf")
    for _ in range(REPEATS):
        data_copy = list(data)
        t0 = time.perf_counter()
        fn(data_copy)
        best = min(best, time.perf_counter() - t0)
    return best

def bench_fib(sizes=(100_000, 1_000_000, 10_000_000)):
    lines = [
        "| n | fib_iterative (s) | fib_recursive (s) |",
        "|---:|---:|---:|",
    ]
    for n in sizes:
        t_iter = _timeit(lambda _: fib_iterative(n), [0])
        
        if n <= 30:
            t_rec = f"{_timeit(lambda _: fib_recursive(n), [0]):.3e}"
        else:
            t_rec = "— (too slow)"
            
        lines.append(f"| {n} | {t_iter:.3e} | {t_rec} |")
    return lines

def bench_sort(generators, sizes=(1_000, 10_000, 100_000)):
    lines = [
        "| generator | n | insertion (s) | merge (s) |",
        "|---|---:|---:|---:|",
    ]
    for gname, gen in generators.items():
        for n in sizes:
            data = gen(n)
            
            if n <= LIMIT_QUADRATIC:
                t_ins = f"{_timeit(insertion_sort, data):.3e}"
            else:
                t_ins = "— (too slow)"
                
            t_mer = f"{_timeit(merge_sort, data):.3e}"
            
            lines.append(f"| {gname} | {n} | {t_ins} | {t_mer} |")
    return lines
