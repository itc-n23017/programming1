data = [
    "01,0001,Male,Yamada,Tarou,25,Tokyo".split(","),
    "01,0002,Male,Satou,Takeshi,27,Kanagawa".split(","),
    "01,0003,Female,Tanaka,Yuko,25,Saitama".split(","),
    "02,0001,Male,Smith,Mike,22,NewJersey".split(","),
    "02,0002,Male,Turner,Tom,27,Kansas".split(","),
    "02,0003,Male,Jackson,David,22,Florida".split(","),
]

member_info = {}
for record in data:
    key = (record[0], record[1])
    info = record[2:]
    member_info[key] = info

print("number", "information", sep="\t")
for key, info in member_info.items():
    print(key, info)
