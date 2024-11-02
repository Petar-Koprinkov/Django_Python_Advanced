import time


def limit_work_time(view_func):
    def wrapper(request, *args, **kwargs):
        start = time.time()
        result = view_func(request, *args, **kwargs)
        end = time.time()

        print(f"The time it took for {view_func.__name__}: ", end - start, "seconds")

        return result

    return wrapper

