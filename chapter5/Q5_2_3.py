a = [x * y for x in range(3) for y in range(x + 1)]
print(a)

print("x", "y", "x*y", sep="\t")
for x in range(3):
    for y in range(x + 1):
        print(x, y, x * y, sep="\t")
