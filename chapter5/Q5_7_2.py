data = [
    ["0001", "Male", "Yamada", "Tarou", 25, "Tokyo"],
    ["0002", "Male", "Satou", "Takeshi", 27, "Kanagawa"],
    ["0003", "Female", "Tanaka", "Yuko", 25, "Saitama"],
    ["0004", "Male", "Suzuki", "Ichiro", 35, "Hokkaido"],
]
member = {}
for record in data:
    key = record[0]
    info = record[1:]
    member[key] = info

print("number", "information", sep="\t")
for key, info in member.items():
    print(key, info)
