#함수 이름은 변경 가능합니다.
student_name = {} #ex){'yeram' : [100, 100]}
grade = 0

##############  menu 1
def Menu1(name, mid, final): #학생들 이름과 점수를 리스트에 보관한다.
    student_name[name] = [mid, final] #dict 요소 추가

##############  menu 2
def Menu2() :
    for key in student_name:
        if len(student_name[key]) == 3: #학점이 있다면
            continue
        else:
            average = (int(student_name[key][0])+int(student_name[key][1]))/2

    if average >= 90:
        student_name[key] = [student_name[key][0], student_name[key][1], 'A']
    if average >= 80:
        student_name[key] = [student_name[key][0], student_name[key][1], 'B']
    if average >= 70:
        student_name[key] = [student_name[key][0], student_name[key][1], 'C']
    else:
        student_name[key] = [student_name[key][0], student_name[key][1], 'D']

##############  menu 3
def Menu3() :
    print('------------------------------------')
    print('name       mid      final      grade')
    print('------------------------------------')
    for key in student_name:
        print(student_name[key], student_name[key][0],student_name[key][1],student_name[key][2])


##############  menu 4
#def Menu4(#매개변수가 필요한지 판단 후 코딩할 것):
    #학생 정보 삭제하는 코딩

#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1": ##@@@@@@예외 하나 남음
        while True:
            try:
                name, mid, final = input('Enter name mid-score final-score : ').split()
                if str.isdigit(mid) == False or str.isdigit(final)== False: # 받은 mid 값을 str인지 확인하고 불린값 출력. 그리고 그 불린값과 False비교해 true면(false와 일치하면) TypeError 발생시킨다.
                    raise TypeError
            except ValueError: # 3개 다 안 쓰면 예외 문구 발생
                print('Num of data is not 3!')
            except TypeError: #정수 입력하지 않으면 예외 문구 발생
                print('Score is not positive integer!')
            else:
                set_data = Menu1(name, mid, final) # 학생 이름과 점수들을 Menu1 함수에 넣는다.
                break
                #학생 정보 입력받기 ok
                #예외사항 처리(데이터 입력 갯수ok, @@@@@이미 존재하는 이름@@@@@, 입력 점수 값이 양의 정수인지ok)
                #예외사항이 아닌 입력인 경우 1번 함수 호출ok

    elif choice == "2" :
        if len(student_name) > 0:
            Menu2()
            print("Grading to all students.")
        else:
            print('No student data!')
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력

    #elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출

    #elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력

    #elif choice == "5" :
        #프로그램 종료 메세지 출력
        #반복문 종료

    #else :
        #"Wrong number. Choose again." 출력