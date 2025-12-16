exam_results = [
    {'student_name': 'Анна', 'score': 91, 'passed': True},
    {'student_name': 'Богдан', 'score': 58, 'passed': False},
    {'student_name': 'Вікторія', 'score': 75, 'passed': True},
    {'student_name': 'Григорія', 'score': 45, 'passed': False}
]

successful_students = []

for student in exam_results:
    if student["passed"] == True:
        successful_students.append(student)

print("Кількість студентів, що склали іспит :" )

