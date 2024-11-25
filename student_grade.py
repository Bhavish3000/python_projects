"""_Convering the scores of students in an dictionary in to grades and storing them in an new dictionary_
    """
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}
for key in student_scores:
    if student_scores[key] in range(91, 100):
        student_grades[key]="Outstanding"
    elif student_scores[key] in range(81, 90):
        student_grades[key]="Exceeds Expectations"
    elif student_scores[key] in range(71, 80):
        student_grades[key]="Acceptable"
    else:
        student_grades[key]="Fail"
print(student_grades)