a = ["1.0,2.2,3.5", "1.2,1.3,2.2", "2.1,3.2,5.5", "2.1,3.1,4.5"]
b, c, d, e = list(map(lambda x: list(map(float, x.split(","))), a))
print(b, c, d, e, sep=",")
