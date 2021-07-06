

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
for current_num in range(1, num + 1):
    print('playerA : %d' %current_num)
    current_num += 1

while True:
    try:
        B_tell_num = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
        if B_tell_num >=4:
            raise TypeError
        break
    except ValueError:
        print('정수를 입력하세요')
    except TypeError:
        print('1, 2, 3만 입력 가능')
        
numB = current_num + B_tell_num
for current_num in range(current_num, numB):
    print('playerB : %d' %current_num)
    current_num += 1
