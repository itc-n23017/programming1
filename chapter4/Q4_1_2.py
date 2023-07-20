def f(n):
    r = [0, 1]
    while (a := r[-2] + r[-1]) < n:
        r.append(a)
    return r


n = int(input())
print(f(n))
