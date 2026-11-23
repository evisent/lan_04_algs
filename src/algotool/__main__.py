import argparse
import sys

from .benchmark import bench_fib, bench_sort
from .errors import AlgoError, QueueEmptyError
from .fib import (
    fib_iterative,
    fib_recursive,
)
from .generators import GENERATORS
from .queue_ds import Queue
from .sort import insertion_sort, merge_sort


def main(argv=None):
    parser = argparse.ArgumentParser(prog="algotool", description="Algorithms and data structures")
    sub = parser.add_subparsers(dest="command", required=True)

    p_fib = sub.add_parser("fib", help="compute Fibonacci number")
    p_fib.add_argument("--n", type=int, required=True)
    p_fib.add_argument(
        "--impl",
        choices=["iterative", "recursive"],
        default="iterative",
    )

    sub.add_parser("queue-demo", help="queue demo")

    p_sort = sub.add_parser("sort", help="sort comma-separated list")
    p_sort.add_argument("--input", required=True)
    p_sort.add_argument("--algo", choices=["insertion", "merge"], required=True)

    p_gen = sub.add_parser("gen", help="generate test data")
    p_gen.add_argument("--type", choices=list(GENERATORS), required=True)
    p_gen.add_argument("--n", type=int, required=True)
    p_gen.add_argument("--seed", type=int, default=0)

    p_bench = sub.add_parser("bench", help="run benchmark")
    p_bench.add_argument("--sizes", default="100000,1000000,10000000")
    p_bench.add_argument("--out", help="write Markdown report to file")

    args = parser.parse_args(argv)

    try:
        if args.command == "fib":
            impl = {
                "iterative": fib_iterative,
                "recursive": fib_recursive,
            }[args.impl]
            print(impl(args.n))

        elif args.command == "queue-demo":
            q = Queue()
            for x in (1, 2, 3):
                q.enqueue(x)
            print("q =", q)
            print("len =", len(q), "bool =", bool(q))
            print("peek =", q.peek())
            print("dequeue =", q.dequeue())
            while q:
                q.dequeue()
            try:
                q.dequeue()
            except QueueEmptyError as e:
                print("empty dequeue ->", type(e).__name__, e)

        elif args.command == "sort":
            data = [int(x) for x in args.input.split(",") if x.strip() != ""]
            fn = {"insertion": insertion_sort, "merge": merge_sort}[args.algo]
            print(",".join(str(x) for x in fn(data)))

        elif args.command == "gen":
            data = GENERATORS[args.type](args.n, seed=args.seed)
            print(",".join(str(x) for x in data))

        elif args.command == "bench":
            sizes = [int(x) for x in args.sizes.split(",")]
            lines = []
            lines.extend(bench_fib(sizes))
            lines.append("")
            lines.extend(bench_sort(GENERATORS, sizes))
            text = "\n".join(lines)
            if args.out:
                with open(args.out, "w", encoding="utf-8") as f:
                    f.write(text + "\n")
                print("written:", args.out)
            else:
                print(text)

    except AlgoError as e:
        print("error:", e, file=sys.stderr)
        return 2
    except (TypeError, ValueError, RecursionError) as e:
        print(f"error: {type(e).__name__}: {e}", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())