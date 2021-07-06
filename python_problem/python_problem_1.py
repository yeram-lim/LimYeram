while True:
    try:
        num = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
        if num >=4:
            raise TypeError
        break
    except ValueError:
        print('정수를 입력하세요')
    except TypeError:
        print('1, 2, 3만 입력 가능')    

current_num = 1
while current_num <= num:
    print('playerA : %d' %current_num)
    current_num += 1

B_tell_num = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
numB = current_num + B_tell_num
while current_num < numB:
    print('playerB : %d' %current_num)
    current_num += 1