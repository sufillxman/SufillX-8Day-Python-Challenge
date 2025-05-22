students = [("Amit", 78), ("Rita", 92), ("Karan", 49), ("Sita", 61), ("John", 35)]

# 1️⃣ Highest Scorer
topper = students[0]
for student in students:
    if student[1] > topper[1]:
        topper = student

print(f"\n🏆 Topper: {topper[0]} with {topper[1]} marks\n")

# 2️⃣ Average Marks
total = 0
for student in students:
    total += student[1]

average = total / len(students)
print(f"📊 Average Marks: {average:.2f}\n")

# 3️⃣ Print Full Scorecard
print("🎯 Student Scorecard:")
print("-" * 30)
for i, (name, marks) in enumerate(students, start=1):
    status = "PASS" if marks >= 50 else "FAIL"
    print(f"{i}. {name:10} | {marks:3} | {status}")
