import random


def generate_students_data(num_students=10):
    students_data = []
    for i in range(num_students):
        name = "n" + str(random.randint(10, 50))
        height = random.randint(150, 190)
        weight = random.randint(50, 80)
        students_data.append((name, height, weight))
        if i == 0:
            print("i, name, height, weight")
        if i < 2 or i == num_students - 1:
            print(i, name, height, weight)
        elif i == 2:
            print("...")
    return students_data


students_data = generate_students_data(10)

students_by_height = sorted(students_data, key=lambda s: s[1])
students_by_weight = sorted(students_data, key=lambda s: s[2])

print("\nSort by height")
for student in students_by_height:
    print(student)


print("\nSort by height")
for student in students_by_weight:
    print(student)
# しょーみ何もわからん
