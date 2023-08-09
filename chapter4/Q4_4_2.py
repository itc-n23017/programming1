n = 0


def vote(x):
    print("1票投票します")
    return x + 1


def reset():
    print("箱を空にしました")
    return 0


def check(x):
    print("ただいまの得票数: {}".format(x))


while True:
    a = input("vote or reset or check: ")
    if a == "vote":
        n = vote(n)
    elif a == "reset":
        n = reset()
    else:
        check(n)
