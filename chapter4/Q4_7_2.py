def f(n):
    m = len(str(n * 9))
    kuku = [" ".join([f"{i*j:{m}d}" for j in range(1, n + 1)]) for i in range(1, 10)]
    return "\n".join(kuku)


print(f(n := int(input("どの段までの掛け算表を表示しますか: "))))
