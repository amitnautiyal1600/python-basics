student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for stu in student_scores:
    grade = ''
    if student_scores[stu] >= 91 :
        grade = 'Outstanding'
    elif student_scores[stu] >= 81 :
        grade = 'Exceeds Expectations'
    elif student_scores[stu] >= 71 :
        grade = 'Acceptable'
    else :
        grade = 'Fail'

    student_grades[stu] = grade

print(student_grades)
