student_name = {'a': [30, 40, 0], 'b': [50, 40, 0]}

def keys_check():
    if len(student_name) == 0: #입력된 것이 없을때(1 실행x)
        print('1')
    for key in student_name.keys(): #키를 돌린다.
        if len(student_name[key]) == 3: #학점까지 모두 있을 때
            continue
        else: #키의 값이 3개 미만인게 있으면
            print('2')
keys_check()
print('suc')