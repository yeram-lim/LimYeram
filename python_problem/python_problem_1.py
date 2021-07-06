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

i = 1
while i <= num:
    print('playerA : %d' %i)
    i += 1