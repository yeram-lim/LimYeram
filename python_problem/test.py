student_name = {'a':[10, 10], 'b':[20,20], 'c':[30,30]} 
grade = 0

def Menu2(i) :
    average = (student_name[i][1]+student_name[i][2])/2
    if average >= 90:
        grade = 'A'
    if average >= 80:
        grade = 'B'
    if average >= 70:
        grade = 'C'
    else:
        grade = 'D'
    student_name[i] = grade

i = 0
try: #각 학생들 인덱스를 돌려서 grade 속에 해당 인덱스가 있는지 없는지 판단. 없으면 함수 추가, 있으면 break
    for i in range(0, len(student_name.keys)):
        if student_name[i][2] != None: #학생이 있다면
            raise IndexError
        else:
            set_data = Menu2(i)
except IndexError:
    print('Grading to all students.')

print(grade)

        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력