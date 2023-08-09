def func():
    def add(x, y):
        return x + y

    return add


adder = func()
answer = adder(1, 10)
print(answer)
