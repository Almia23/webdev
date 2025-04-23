def student():
    s = input("Name RollNo Dept Addr Gender Marks1 Marks2 Marks3: ").split()
    name, marks = s[0], list(map(int, s[5:]))
    total, pct = sum(marks), sum(marks)/3
    print(f"{s[:5]}, Total: {total}, %: {pct}")
    return name, total, any(m<10 for m in marks)

students = [student() for _ in range(3)]
print("Max:", max(students, key=lambda x:x[1])[0])
print("Min:", min(students, key=lambda x:x[1])[0])
print("Fails:", [s[0] for s in students if s[2]])