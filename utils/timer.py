import time
import functools


def time_me(func):
    def wrap(*args, **kwargs):
        s = time.time()
        res = func(*args, **kwargs)
        print("elapsed exec time: {}".format(time.time() - s))
        return res
    return wrap


def _benchmark_run(num_runs, function, *args, **kwargs):
    runs = []
    res = None
    for _ in range(num_runs):
        s = time.time()
        res = function(*args, **kwargs)
        elapsed = time.time() - s
        runs.append(elapsed)

    slowest_run_time = max(runs)
    fastest_run_time = min(runs)
    avg_run_time = sum(runs) / len(runs)
    sep = "*" * 40
    print("\n{}\n  -- After {} runs -- \nAvg Run Time: {}\nSlowest Run: {}\nFastest Run: {}\n{}\n".format(
        sep,
        num_runs,
        avg_run_time,
        slowest_run_time,
        fastest_run_time,
        sep,
    ))
    return res


def benchmark(arg=None):
    @functools.wraps(arg)
    def _decorate(*args, **kwargs):
        if callable(arg):
            return _benchmark_run(10, arg, *args, **kwargs)

        # if arg is the num runs, then inner *args[0] will be the function we wrap around
        function = args[0]
        num_runs = arg if arg is not None else 10

        def _inner(*func_args, **func_kwargs):
            return _benchmark_run(num_runs, function, *func_args, **func_kwargs)
        return _inner

    return _decorate
