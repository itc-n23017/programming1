def f_s(*args):
    return [i**2 for i in args]


print(f_s(*[1, 2, 3, 4]))
print(f_s(*list(range(100))))
