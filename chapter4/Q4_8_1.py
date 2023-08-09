import time


def show_begin_end(func):
    def deco_func(*args, **kwargs):
        print("== start")
        result = func(*args, **kwargs)
        result
        print("== end")

    return deco_func


@show_begin_end
def sleep_for_a_while():
    print("Sleeping")
    time.sleep(2)
    print("Done Sleeping")


sleep_for_a_while()
