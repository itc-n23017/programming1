def f(n=100):
    r = [3, 0, 2]
    while (a := r[-3] + r[-2]) < n:
        r.append(a)
    return r


n = int(input())
print(f(n))
