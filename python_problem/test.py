student_name = {'a': [30, 40, 0], 'b': [50, 40, 0]}

def Menu2() :
    for key in student_name:
        if len(student_name[key]) == 3: #학점이 있다면
            continue
        else:
            average = (int(student_name[key][0])+int(student_name[key][1]))/2
    if average >= 90:
        student_name[key] = [student_name[key][0], student_name[key][1], 'A']
    elif average >= 80:
        student_name[key] = [student_name[key][0], student_name[key][1], 'B']
    elif average >= 70:
        student_name[key] = [student_name[key][0], student_name[key][1], 'C']
    else:
        student_name[key] = [student_name[key][0], student_name[key][1], 'D']